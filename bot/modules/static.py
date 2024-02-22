WelcomeText = \
"""
Hi **%(first_name)s** 😎
I'm Telegram File To Link Generator Bot

Send Me Any File And Get High-Speed Direct Download Link And Streamable Link
- /start to get this message.
- /info to get user info.
- /log to get bot logs. (admin only!)
"""

UserInfoText = \
"""
**First Name:**
`{sender.first_name}`

**Last Name:**
`{sender.last_name}`

**User ID:**
`{sender.id}`

**Username:**
`@{sender.username}`
"""

FileLinksText = \
"""
**File Name:** %(file_name)s
**Download Link:**
<a href="%(dl_link)s">Download</a>
"""

MediaLinksText = \
"""
**Media Name:** %(media_name)s
**Download Link:**
<a href="%(dl_link)s">Download</a>
**Stream Link:**
<a href="%(stream_link)s">Stream</a>
"""

InvalidQueryText = \
"""
Query data mismatched.
"""

MessageNotExist = \
"""
File revoked or not exist.
"""

LinkRevokedText = \
"""
The link has been revoked. It may take some time for the changes to take effect.
"""

InvalidPayloadText = \
"""
Invalid payload.
"""

MediaTypeNotSupportedText = \
"""
Sorry, this media type is not supported.
"""
