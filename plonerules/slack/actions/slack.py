from Acquisition import aq_inner
from OFS.SimpleItem import SimpleItem
from zope.component import adapts
from zope.component.interfaces import ComponentLookupError
from zope.interface import Interface, implements
from zope.formlib import form

from zope.app.form import CustomWidgetFactory
from zope.app.form.browser import ObjectWidget
from zope.app.form.browser import ListSequenceWidget

from plone.app.contentrules.browser.formhelper import AddForm, EditForm 
from plone.contentrules.rule.interfaces import IRuleElementData, IExecutable

from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import safe_unicode

from plonerules.slack.actions.interfaces import ISlackAction
from slacker import Slacker



class SlackAction(SimpleItem):
    """
    The implementation of the action defined in ISlackAction
    """
    implements(ISlackAction, IRuleElementData)

    chanel = '' #unicode paths are not allowed
    token = ''
    emoji = ''    
    element = 'plone.actions.Slack'
    message = u''

    @property
    def summary(self):
        return "Post to %s chanel on slack" % self.chanel


class SlackActionExecutor(object):
    """The executor for this action.
    """
    implements(IExecutable)
    adapts(Interface, ISlackAction, Interface)

    def __init__(self, context, element, event):
        self.context = context
        self.element = element
        self.event = event

    def __call__(self):

        obj = self.event.object
        event_title = safe_unicode(obj.Title())
        event_url = obj.absolute_url()
        
        slack = Slacker(self.element.token)

        message = self.element.message.replace("${url}", event_url)
        message = message.replace("${title}", event_title)
        try:
            slack.chat.post_message(self.element.chanel, message, username=None, parse=None,
                     link_names=None, attachments=None, unfurl_links=None,
                     icon_url=None, icon_emoji=self.element.emoji)
        except:
            return False        
        return True

class SlackAddForm(AddForm):
    """
    An add form for the Slack action
    """
    form_fields = form.FormFields(ISlackAction)
    
    label = u"Add Slack Action"
    description = u"An action that can post on slack chanel"
    form_name = u"Configure element"

    def create(self, data):
        a = SlackAction()
        form.applyChanges(a, self.form_fields, data)
        return a
    
    #TODO: automatically fill parameter list. 
    # is this really usefull? what if script cant be traversed to at config time?
    # what if script is a view instead?
    #def getScriptParams(self, script_name):
    #    script.ZScriptHTML_tryParams()

class SlackEditForm(EditForm):
    """
    An edit form for the Slack action
    """
    form_fields = form.FormFields(ISlackAction)
    
    label = u"Edit Slack Action"
    description = u"An action that can post on slack chanel"
    form_name = u"Configure element"
