import React from 'react';

import Slarf, { type SlarfElement, type Primitive } from 'slarf';
import { SlarfOptions } from 'slarf/types';
import { capitalizeFirstLetter } from 'slarf/utils';

type ReactElement = ReturnType<typeof React.createElement<Record<string, any>>>;

export let SlarfContext: React.Context<SlarfReact>;

export function createContext(config?: SlarfOptions): React.Context<SlarfReact> {
    if (!SlarfContext) {
        SlarfContext = React.createContext(new SlarfReact(config));
    }

    return SlarfContext;
}

class SlarfReact extends Slarf {
    private convertToReact(element: SlarfElement | Primitive): ReactElement | Primitive {
        if (this.isPrimitive(element)) {
            return element;
        }

        if ('slarf:id' in element.props) {
            const events: string[] = element.props['slarf:events']?.split(',') || [];
            events.forEach((event) => {
                event = capitalizeFirstLetter(event);
                element.props[`on${event}`] = (e: Event) => {
                    this.emit(
                        'dom_event',
                        `${element.props['slarf:id']}:${event}`,
                        {
                            slarfId: element.props['slarf:id'],
                            event: this.serializeEventObject(e),
                        }
                    );
                };
            });
        }

        const children = (
            Array.isArray(element.children) ? element.children : [element.children]
        ).map((child: SlarfElement | Primitive) => this.convertToReact(child));
        return React.createElement(element.type, element.props, ...children);
    }
}

function canRender(component: unknown): component is SlarfElement {
    return typeof component === 'object'
        && component !== null
        && Object.prototype.hasOwnProperty.call(component, 'type')
        && Object.prototype.hasOwnProperty.call(component, 'props');
}

function render(component: any) {
    if (canRender(component)) {
        const children: ReactElement[] = Array.isArray(component.children) ? component.children.map(render) : [];
        return React.createElement(component.type, component.props, ...children);
    }
    return component;
}

interface SlarfComponentProps {
    name: string;
    props?: Record<string, any>;
}

export function SlarfComponent({ name, props = {} }: SlarfComponentProps) {
    const componentsApi = React.useContext(SlarfContext);
    const [component, setComponent] = React.useState<SlarfElement | Primitive>(null);

    React.useEffect(() => {
        const fetchComponent = async () => {
            const component = await componentsApi.getComponent(name, props);
            setComponent(component);
        };

        fetchComponent();
    }, [name, props, componentsApi]);

    return component && render(component);
}
