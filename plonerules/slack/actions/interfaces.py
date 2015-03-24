from zope.interface import Interface
from zope import schema


class ISlackAction(Interface):
    """Definition of the configuration available for a Slack action"""
    
    chanel = schema.TextLine(
        title=u"Channel",
        description=u"The channel to post",
        required=True
    )
    token = schema.TextLine(
        title=u"Webhook Token",
        description=u"The token (available in API settings on slack)",
        required=True
    )
    emoji = schema.TextLine(
        title=u"emoji to use",
        description=u"An emoji picked in http://www.emoji-cheat-sheet.com/ (ex: ':dash:')",
        required=True
    )
     
    message = schema.Text(
        title=u"Message",
        description=u"Type in here the message that you \
want to post. Some defined content can be replaced: ${title} will be replaced \
by the title of the newly created item. ${url} will be replaced by the \
URL of the newly created item.",
        required=True)