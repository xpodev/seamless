import React from 'react';

import BaseJSX, { type PyJSXElement, type Primitive } from 'slarf';
import { SlarfOptions } from 'slarf/types';
import { capitalizeFirstLetter } from 'slarf/utils';

type ReactElement = ReturnType<typeof React.createElement<Record<string, any>>>;


export let PyJSXContext: React.Context<PyJSX>;


export function createContext(config?: SlarfOptions): React.Context<PyJSX> {
    if (!PyJSXContext) {
        PyJSXContext = React.createContext(new PyJSX(config));
    }

    return PyJSXContext;
}

class PyJSX extends BaseJSX {
    private convertToReact(element: PyJSXElement | Primitive): ReactElement | Primitive {
        if (this.isPrimitive(element)) {
            return element;
        }

        if ('jsx:id' in element.props) {
            const events: string[] = element.props['jsx:events']?.split(',') || [];
            events.forEach((event) => {
                event = capitalizeFirstLetter(event);
                element.props[`on${event}`] = (e: Event) => {
                    this.emit(
                        'dom_event',
                        `${element.props['jsx:id']}:${event}`,
                        {
                            jsxId: element.props['jsx:id'],
                            event: this.serializeEventObject(e),
                        }
                    );
                };
            });
        }

        const children = (
            Array.isArray(element.children) ? element.children : [element.children]
        ).map((v) => this.convertToReact(v));
        return React.createElement(element.type, element.props, ...children);
    }
}

function canRender(component: unknown): component is PyJSXElement {
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

interface PyComponentProps {
    name: string;
    props?: Record<string, any>;
}

export function PyComponent({ name, props = {} }: PyComponentProps) {
    const componentsApi = React.useContext(PyJSXContext);
    const [component, setComponent] = React.useState<PyJSXElement | Primitive>(null);

    React.useEffect(() => {
        const fetchComponent = async () => {
            const component = await componentsApi.getComponent(name, props);
            setComponent(component);
        };

        fetchComponent();
    }, [name, props, componentsApi]);

    return component && render(component);
}
