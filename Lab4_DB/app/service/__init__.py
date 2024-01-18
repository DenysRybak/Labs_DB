
from .agencies_service import AgenciesService
from .agency_region_service import AgencyRegionService
from .animator_event_type_service import AnimatorEventTypeService
from .animators_agencies_service import AnimatorsAgenciesService
from .animators_service import AnimatorsService
from .order_agencies_service import OrderAgenciesService
from .order_animators_service import OrderAnimatorsService
from .order_days_service import OrderDaysService
from .orders_service import OrderService
from .type_events_service import TypeEventsService


agencies_service = AgenciesService()
agency_region_service = AgencyRegionService()
animator_event_type_service = AnimatorEventTypeService()
animators_agencies_service = AnimatorsAgenciesService()
animators_service = AnimatorsService()
order_agencies_service = OrderAgenciesService()
order_animators_service = OrderAnimatorsService()
order_days_service = OrderDaysService()
orders_service = OrderService()
type_events_service = TypeEventsService()