import { default as _PyJSX } from 'py-jsx';
import { capitalizeFirstLetter } from 'py-jsx/utils'
import type { PyJSXElement, Primitive } from 'py-jsx';
import React from 'react';

type ReactElement = ReturnType<typeof React.createElement<Record<string, any>>>;

export let PyJSXContext: React.Context<PyJSX> = null as any;

export function createContext(config?: any) {
    if (!PyJSXContext) {
        PyJSXContext = React.createContext(new PyJSX());
    }

    return PyJSXContext
}

class PyJSX extends _PyJSX {
    private convertToReact(element: PyJSXElement | Primitive): ReactElement | Primitive {
        if (this.isPrimitive(element)) {
            return element;
        }

        if ('jsx:id' in element.props) {
            const events: string[] = element.props['jsx:events']?.split(',') || [];
            events.forEach((event) => {
                event = capitalizeFirstLetter(event);
                element.props[`on${event}`] = (e: any) => {
                    this.emit(
                        'dom_event',
                        `${element.props['jsx:id']}:${event}`,
                        {
                            jsxId: element.props['jsx:id'],
                            foo: 'bar',
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

function canRender(component: any): component is PyJSXElement {
    return typeof component === 'object' && component !== null && component.hasOwnProperty('type') && component.hasOwnProperty('props');
}

function render(component: any) {
    if (canRender(component)) {
        const children: any[] = Array.isArray(component.children) ? component.children.map(render) : [];
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
