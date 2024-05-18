css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div style="display:flex;" class="avatar">
        <img src="https://i.ibb.co/SXQxw5B/chatbot-1.png" style="max-height: 32px; max-width: 32px; border-radius: 50%; object-fit: cover;">
        <div class="message">{{MSG}}</div>
    </div>
    
</div>
<br><br>
'''


user_template = '''
<div class="chat-message user">
    <div style="display:flex;" class="avatar">
        <img src="https://i.ibb.co/nfrQMd0/working.png" style="max-height: 32px; max-width: 32px; border-radius: 50%; object-fit: cover;">
        <div class="message">{{MSG}}</div>
    </div>    
    
</div>
'''
