
from .animators_dao import AnimatorDAO
from .orders_dao import OrderDAO
from .agencies_dao import AgencyDAO
from .type_events_dao import TypeEventDAO
from .animators_agencies_dao import AnimatorsAgenciesDAO
from .agency_region_dao import AgencyRegionDAO
from .animator_event_type_dao import AnimatorEventTypeDAO
from .order_agencies_dao import OrderAgenciesDAO
from .order_days_dao import OrderDaysDAO
from .order_animators_dao import OrderAnimatorsDAO


animators_dao = AnimatorDAO()
orders_dao = OrderDAO()
agencies_dao = AgencyDAO()
type_events_dao = TypeEventDAO()
animators_agencies_dao = AnimatorsAgenciesDAO()
agency_region_dao = AgencyRegionDAO()
animator_event_type_dao = AnimatorEventTypeDAO()
order_agencies_dao = OrderAgenciesDAO()
order_days_dao = OrderDaysDAO()
order_animators_dao = OrderAnimatorsDAO()

