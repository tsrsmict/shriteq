from django_components import component
print('Hello')
@component.register("event")
class Event(component.Component):
    template_name = "event/event.html"

    def get_context_data(self, event_name, event_short_desc, event_participation_reqs, event_elig):
        return {
            "event_name": event_name,
            "event_short_desc": event_short_desc,
            "event_participation_reqs": event_participation_reqs,
            "event_elig": event_elig
        }