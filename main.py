from flet import *
import bcrypt as bc
import uvicorn
import SYSConnectToServers as CS


class LoginScreen(Container):

    def __init__(self, page):
        super().__init__()
        self.page = page
        self.ODS = CS.ConnectToODSServer()
        self.salt = bc.gensalt()
        self.GetLoginScreen()
        self.LoginScreen =  Container(expand=True,content=Row(controls=[(Column([self.username, self.password, self.signup, self.submit],
                            alignment=MainAxisAlignment.CENTER))],alignment=MainAxisAlignment.CENTER))

    def GetLoginScreen(self):
        self.username = TextField(border_color="#AD1457", label='Username',color='white', text_align=TextAlign.LEFT, height=40, width=200)
        self.password = TextField(border_color="#AD1457", label='Password', color='white', text_align=TextAlign.LEFT,height=40, width=200,
                        password=True, can_reveal_password=True,on_change=self.GetValidation)
        self.signup = Container(height=20)
        # self.signup = Checkbox(label='I agree to stuff', check_color='#AD1457',value=False, on_change=self.GetValidation)
        self.submit = ElevatedButton(text='Login', bgcolor="#AD1457", color='white', height=40, width=200, on_click=self.GetSubmit, disabled=True)

    def GetValidation(self, e):
        # if all([self.username.value, self.password.value, self.signup.value]): self.submit.disabled = False
        if all([self.username.value, self.password.value]): self.submit.disabled = False
        else: self.submit.disabled = True
        self.LoginScreen.update()

    def GetSubmit(self, e):
        StoredPsswd = str(self.ODS.qryODSGetData(f"select HashedPassword from ETLUserData where UserName = '{self.username.value}'").values[0][0])
        StoredPsswd = StoredPsswd.encode("utf-8")
        EnteredPsswd = self.password.value.encode("utf-8")
        if bc.checkpw(EnteredPsswd, StoredPsswd): print("Password is Correct")
        else: print("Password is Incorrect")

def main(page: Page):

    page.title = "Signup"
    page.bgcolor = Colors.BLACK
    page.add(LoginScreen(page).LoginScreen)
    page.update()

if __name__ == "__main__":
    app(main, view=AppView.WEB_BROWSER)







