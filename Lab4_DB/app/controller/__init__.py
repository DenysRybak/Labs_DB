
from .agencies_controller import AgencyController
from .agency_region_controller import AgencyRegionController
from .animator_event_type_controller import AnimatorEventTypeController
from .animators_agencies_controller import AnimatorsAgenciesController
from .animators_controller import AnimatorController
from .order_agencies_controller import OrderAgenciesController
from .order_animators_controller import OrderAnimatorsController
from .order_days_controller import OrderDaysController
from .orders_controller import OrderController
from .type_events_controller import TypeEventController



agencies_controller = AgencyController()
agency_region_controller = AgencyRegionController()
animator_event_type_controller = AnimatorEventTypeController()
animators_agencies_controller = AnimatorsAgenciesController()
animators_controller = AnimatorController()
order_agencies_controller = OrderAgenciesController()
order_animators_controller = OrderAnimatorsController()
order_days_controller = OrderDaysController()
orders_controller = OrderController()
type_events_controller = TypeEventController()