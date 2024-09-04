from pydom.context.standard import add_standard_features as pydom_standard_features


from .context import Context
from ..extra.components import ComponentsFeature
from ..extra.events import EventsFeature
from ..extra.state import StateFeature
from ..extra.transformers.js_transformer import init_transformer, js_transformer
from ..extra.transports.socketio.transport import SocketIOTransport


def add_standard_features(ctx: Context):
    pydom_standard_features(ctx)

    ctx.add_feature(SocketIOTransport)
    ctx.add_feature(ComponentsFeature)
    ctx.add_feature(EventsFeature)
    ctx.add_feature(StateFeature)

    ctx.add_prop_transformer(*init_transformer())
    ctx.add_prop_transformer(*js_transformer())
