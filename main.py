import unittest
from time import sleep
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


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

    #Cards
    tvTitle = "com.lovina.android:id/tvTitle"
    tvMessage = "com.lovina.android:id/tvMessage"
    btnGotIt = "com.lovina.android:id/btnGotIt"
    btnUserActionSuperLike = "com.lovina.android:id/btnUserActionSuperLike"
    btnUserActionLike = "com.lovina.android:id/btnUserActionLike"
    btnUserActionDisLike = "com.lovina.android:id/btnUserActionDisLike"


    #Profile
    btnEditProfile = "com.lovina.android:id/btnEditProfile"
    btnSettings = "com.lovina.android:id/btnSettings"
    idAvatar = "com.lovina.android:id/ivAvatar"
    btnBoost = "com.lovina.android:id/btnBoost"
    btnCoins = "com.lovina.android:id/btnCoins"

    btnRemove = "com.lovina.android:id/btnRemove"
    tvAboutMeCounter = "com.lovina.android:id/tvAboutMeCounter"
    etAboutMe = "com.lovina.android:id/etAboutMe"
    ivToolbarRightIcon = "com.lovina.android:id/ivToolbarRightIcon"

    btnContinue = "com.lovina.android:id/btnContinue"
    ivToolbarLeftIcon = "com.lovina.android:id/ivToolbarLeftIcon"

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

    def loginbyVK(self):

        self.driver.find_element_by_id(self.VkLogin).click()
        self.driver.implicitly_wait(400)
        self.driver.find_element_by_id(self.allowbtn).click()
        self.driver.find_element_by_id(self.permission_allow_button).click()

        sleep(1)
        assert self.driver.current_activity == ".ui.activity.main.MainActivity", "Неверная активность"

    def test_01_loginbyPhone(self):

        self.driver.find_element_by_id(self.LoginPhone).click()
        self.driver.find_element_by_id(self.permission_allow_button).click()
        self.driver.find_element_by_id(self.etPhoneNumber).send_keys("9270143434")
        self.driver.find_element_by_xpath(self.NextButton).click()
        sleep(10)
        self.driver.find_element_by_id(self.etSmsCode).send_keys(input())
        self.driver.find_element_by_xpath(self.NextButton).click()
        self.driver.find_element_by_id(self.permission_allow_button).click()
        sleep(1)
        assert str(self.driver.current_activity) == ".ui.activity.main.MainActivity", "Неверная активность"

    def test_02_tutorials(self):

        self.driver.swipe(0, 0, 800, 0, 500)
        assert self.driver.find_element_by_id(self.tvTitle).text == "Нравится", "Неверный текст заголовка в туториале"
        assert self.driver.find_element_by_id(self.tvMessage).text == "Если профиль понравился, смахните вправо и ждите взаимный лайк", "Неверный текст туториала"
        self.driver.find_element_by_id(self.btnGotIt).click()

        sleep(1)
        self.driver.swipe(800, 0, 0, 0, 500)
        assert self.driver.find_element_by_id(self.tvTitle).text == "Не нравится", "Неверный текст заголовка в туториале"
        assert self.driver.find_element_by_id(self.tvMessage).text == "Если профиль вам не понравился, просто смахните влево", "Неверный текст туториала"
        self.driver.find_element_by_id(self.btnGotIt).click()

        sleep(1)
        self.driver.save_screenshot("SuperLikeTutorial.png")
        self.driver.find_element_by_id(self.btnGotIt).click()
        sleep(1)

        while self.driver.find_elements_by_id(self.btnUserActionSuperLike) == 0:
            self.driver.swipe(500, 200, 500, 400)
            sleep(1)

        self.driver.save_screenshot("card.png")

    def profile_edit(self):
        self.driver.find_element_by_xpath(self.Profile_tab).click()
        self.driver.find_element_by_id(self.btnEditProfile).click()

        elements = self.driver.find_elements_by_id(self.btnRemove)
        elements[0].click()

        elements[1].click()

        self.driver.find_elements_by_id(self.permission_allow_button)
        self.driver.find_elements_by_id(self.permission_allow_button)

        element = self.driver.find_elements_by_id("com.lovina.android:id/text1")
        element[1].click()

        sleep(30) #Выбираем фотки за 30 секунд

        self.driver.save_screenshot("Crop.png")
        self.driver.find_element_by_id("com.lovina.android:id/menu_crop")
        self.driver.save_screenshot("New photo.png")

        self.driver.find_element_by_id(self.etAboutMe).click()
        self.driver.find_element_by_id(self.etAboutMe).clear()

        assert self.driver.find_element_by_id(self.tvAboutMeCounter) == 0, "Счетчик символов поля 'О себе' работает некорректно"

        self.driver.find_element_by_id(self.etAboutMe).send_keys("About")

        assert self.driver.find_element_by_id(self.tvAboutMeCounter) == 5, "Счетчик символов поля 'О себе' работает некорректно"

        self.driver.find_element_by_id(self.ivToolbarRightIcon).click()

    def buy(self):
        self.driver.find_element_by_xpath(self.Profile_tab).click()

        self.driver.find_element_by_id(self.btnCoins).click()
        self.driver.save_screenshot("Coins.png")
        self.driver.find_element_by_id(self.btnContinue).click()
        self.driver.find_element_by_accessibility_id("OK")
        self.driver.find_element_by_id(self.ivToolbarLeftIcon).click()

        self.driver.find_element_by_id(self.btnBoost).click()
        self.driver.save_screenshot("Boost.png")
        self.driver.find_element_by_id(self.btnContinue).click()
        self.driver.find_element_by_accessibility_id("OK")
        self.driver.find_element_by_id(self.ivToolbarLeftIcon).click()


    def ProfileView(self):
        self.driver.find_element_by_xpath(self.Profile_tab).click()
        self.driver.find_element_by_id(self.idAvatar).click()




if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LovinaTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
