import unittest

from appium import webdriver


class LovinaTests(unittest.TestCase):

    VkLogin = "com.lovina.android:id/btnVkLogin"
    LoginPhone = "com.lovina.android:id/btnLoginPhone"
    allowbtn = "allow_btn"
    permission_allow_button = "com.android.packageinstaller:id/permission_allow_button"
    etPhoneNumber = "com.lovina.android:id/etPhoneNumber"
    NextButton = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.Button[2]"
    etSmsCode = "com.lovina.android:id/etSmsCode"
    rvCards = "com.lovina.android:id/rvCards"
    btnCardSuperLike = "com.lovina.android:id/btnCardSuperLike"

    #Tabbar
    Profile_tab = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.ImageView[1]"
    Cards_tab = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.ImageView[2]"
    Video_tab = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.ImageView[3]"
    Messages_tab = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.ImageView[4]"

    #Tutorial
    tvTitle = "com.lovina.android:id/tvTitle"
    tvMessage = "com.lovina.android:id/tvMessage"
    btnGotIt = "com.lovina.android:id/btnGotIt"

    #Profile
    btnEditProfile = "com.lovina.android:id/btnEditProfile"
    btnSettings = "com.lovina.android:id/btnSettings"
    idAvatar = "com.lovina.android:id/ivAvatar"
    btnBoost = "com.lovina.android:id/btnBoost"
    btnCoins = "com.lovina.android:id/btnCoins"

    tvAboutMeCounter = "com.lovina.android:id/tvAboutMeCounter"
    etAboutMe = "com.lovina.android:id/etAboutMe"

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'CB512DPQK5'
        #desired_caps['app'] = 'C:\\Users\\littl\\PycharmProjects\\LovinaCheck\\lovina.apk'
        desired_caps['appPackage'] = 'com.lovina.android'
        desired_caps['appActivity'] = '.ui.activity.main.MainActivity'
        #desired_caps['appWaitActivity'] = '.ui.activity.login.LoginActivity'
        desired_caps['unicodeKeyboard'] = 'true'
        desired_caps['noReset'] = 'true'
        #desired_caps['fullReset'] = 'true'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


    def tearDown(self):
        # end the session
        #self.driver.reset()
        self.driver.quit()

    def test_01_loginbyVK(self):

        self.driver.find_element_by_id(self.VkLogin).click()
        self.driver.implicitly_wait(400)
        self.driver.find_element_by_id(self.allowbtn).click()
        self.driver.find_element_by_id(self.permission_allow_button).click()

        self.driver.find_element_by_id(self.rvCards)

    def loginbyPhone(self):
        self.driver.find_element_by_id(self.LoginPhone).click()
        self.driver.find_element_by_id(self.permission_allow_button).click()
        self.driver.find_element_by_id(self.etPhoneNumber).send_keys("9270143434")
        self.driver.find_element_by_xpath(self.NextButton).click()
        self.driver.find_element_by_id(self.etSmsCode).send_keys("0000")

    def test_02_tutorials(self):

        self.driver.swipe(0, 0, 800, 0)
        self.driver.implicitly_wait(240)
        self.driver.save_screenshot("Liked tutorial.png")
        assert self.driver.find_element_by_id(self.tvTitle).text == "Нравится", "Неверный текст заголовка в туториале"
        assert self.driver.find_element_by_id(self.tvMessage).text == "Если профиль понравился, смахните вправо и ждите взаимный лайк", "Неверный текст туториала"
        self.driver.find_element_by_id(self.btnGotIt).click()

        self.driver.swipe(800, 0, 0, 0)
        self.driver.implicitly_wait(240)
        self.driver.save_screenshot("Not liked tutorial.png")
        assert self.driver.find_element_by_id(self.tvTitle).text == "Не нравится", "Неверный текст заголовка в туториале"
        assert self.driver.find_element_by_id(self.tvMessage).text == "Если профиль вам не понравился, просто смахните влево", "Неверный текст туториала"
        self.driver.find_element_by_id(self.btnGotIt).click()

        self.driver.implicitly_wait(240)
        self.driver.save_screenshot("SuperLike.png")
        assert self.driver.find_element_by_id(self.tvTitle).text == "Суперлайк доступен!", "Неверный текст заголовка в туториале"
        assert self.driver.find_element_by_id(self.tvMessage).text == "Ставьте Суперлайк, когда вам кто-то очень понравился: станете первым в списке и он получит уведомление","Неверный текст туториала"
        self.driver.find_element_by_id(self.btnGotIt).click()

    def ProfileEdit(self):
        pass


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LovinaTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
