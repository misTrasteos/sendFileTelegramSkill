from opsdroid.skill import Skill
from opsdroid.matchers import match_regex
from opsdroid.events import File

class SendFileToTelegramSkill(Skill):

    @match_regex(r'!file')
    async def sendDocument(self, message):

        path= 'file.pdf'

        with open(path, 'rb') as file:
            fileEvent = File(file_bytes= file, target= {'id': message.target}, mimetype= 'application/pdf')

            await message.respond( fileEvent )
