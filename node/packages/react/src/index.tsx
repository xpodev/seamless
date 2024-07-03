import React from 'react';

import Seamless, {
    type SeamlessElement,
    type Primitive,
    type SeamlessOptions
} from 'seamless-core';

import { capitalizeFirstLetter } from './utils';

type ReactElement = ReturnType<typeof React.createElement<Record<string, any>>>;

export let SeamlessContext: React.Context<SeamlessReact>;

export function createContext(config?: SeamlessOptions): React.Context<SeamlessReact> {
    if (!SeamlessContext) {
        SeamlessContext = React.createContext(new SeamlessReact(config));
    }

    return SeamlessContext;
}

class SeamlessReact extends Seamless {
    render(element: SeamlessElement | Primitive, parentElement?: ReactElement): ReactElement {
        if (this.isPrimitive(element)) {
            return React.createElement(React.Fragment, null, element);
        }

        if ('seamless:id' in element.props) {
            const events: string[] = element.props['seamless:events']?.split(',') || [];
            events.forEach((event) => {
                event = capitalizeFirstLetter(event);
                element.props[`on${event}`] = (e: Event) => {
                    this.emit(
                        'dom_event',
                        `${element.props['seamless:id']}:${event}`,
                        {
                            seamlessId: element.props['seamless:id'],
                            event: this.serializeEventObject(e),
                        }
                    );
                };
            });
        }

        const children = (
            Array.isArray(element.children) ? element.children : [element.children]
        ).map((child: SeamlessElement | Primitive) => this.render(child));
        return React.createElement(element.type, element.props, ...children);
    }
}

interface SeamlessComponentProps {
    name: string;
    props?: Record<string, any>;
}

export function SeamlessComponent({ name, props = {} }: SeamlessComponentProps) {
    const componentsApi = React.useContext(SeamlessContext);
    const [component, setComponent] = React.useState<ReactElement>(<></>);

    React.useEffect(() => {
        const fetchComponent = async () => {
            const component = await componentsApi.getComponent(name, props);
            setComponent(componentsApi.render(component));
        };

        fetchComponent();
    }, [name, props, componentsApi]);

    return component;
}
