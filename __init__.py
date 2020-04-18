from opsdroid.skill import Skill
from opsdroid.matchers import match_regex
from opsdroid.events import File

class SendFileToTelegramSkill(Skill):

    @match_regex(r'Please, send me a pdf file')
    async def sendDocument(self, message):
        path= '/file.pdf' # This is just for testing purposes, and it must point to a file in your file system. Not in the git repository.

        with open(path, 'rb') as file:
            fileEvent = File(file_bytes= file, mimetype= 'application/pdf', target= {'id': message.target})
            await message.respond( fileEvent )
