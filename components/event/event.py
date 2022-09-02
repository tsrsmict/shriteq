from django_components import component
print('Hello')
@component.register("event")
class Event(component.Component):
    template_name = "templates/event.html"

    def get_context_data(self, style, event_name, event_link, event_short_desc, event_participation_reqs, event_elig):
        return {
            "style": style,
            "event_name": event_name,
            "event_short_desc": event_short_desc,
            "event_participation_reqs": event_participation_reqs,
            "event_elig": event_elig,
            "event_link": event_link
        }