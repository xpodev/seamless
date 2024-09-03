from pydom.context.standard import add_standard_features as pydom_standard_features


from .context import Context
from ..extra.components import ComponentsFeature
from ..extra.events import EventsFeature
from ..extra.state import StateFeature

from ..extra.transformers.class_transformer import class_transformer
from ..extra.transformers.dash_transformer import dash_transformer
from ..extra.transformers.js_transformer import init_transformer, js_transformer
from ..extra.transformers.html_events_transformer import html_events_transformer
from ..extra.transformers.simple_transformer import simple_transformer
from ..extra.transformers.style_transformer import style_transformer

if TYPE_CHECKING:
    from . import Context


def add_standard_features(ctx: Context):
    pydom_standard_features(ctx)

    ctx.add_feature(ComponentsFeature)
    ctx.add_feature(EventsFeature, claim_time=30)
    ctx.add_feature(StateFeature)

    ctx.add_prop_transformer(*init_transformer())
    ctx.add_prop_transformer(*js_transformer())
