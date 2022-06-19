# MrSploit
from time import sleep

from selenium import webdriver

from info import username, password

# LOGIN


class Bot:
    def __init__(self):
        self.login(username, password)

    def login(self, username, password):
        self.driver = webdriver.Firefox()
    # GET SITE
        self.driver.get("https://instagram.com")
        sleep(1)
    # ENTER USERNAME
        user_input = self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input"
        )
        user_input.send_keys(username)
        sleep(2)
    # ENTER PASSWORD
        pass_input = self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input"
        )
        pass_input.send_keys(password)
    # LOGIN BUTTUN
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div"
        ).click()
        sleep(6)
    # LIST USERS
        self.driver.get(
            'https://www.instagram.com/accounts/access_tool/current_follow_requests')
        sleep(1)
        # VIEW MORE..
        # self.driver.find_element_by_xpath(
        # '/html/body/div[1]/section/main/div/article/main/button').click()

        # LIST USERNAME
        list_of_username = []
        for names in self.driver.find_elements_by_class_name('-utLf'):
            list_of_username.append(names.text)

    # print(list_of_username)

    # UNFOLLOW
        for i in list_of_username:
            # GET USER PAGE
            self.driver.get(f'https://instaram.com/{i}')
            sleep(1)
            # REQUEST BUTTUN
            self.driver.find_element_by_xpath(
                '/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/button').click()
            sleep(1)
            # UNFOLLOW BUTTUN
            self.driver.find_element_by_xpath(
                '/html/body/div[5]/div/div/div/div[3]/button[1]').click()


def main():
    myBot = Bot()


if __name__ == "__main__":
    main()
