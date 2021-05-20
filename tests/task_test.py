from src.task import Task
import unittest
from src.task_decider import get_preferred_option


class TestTask(unittest.TestCase):

    def setUp(self):
        self.task_clean_windows = Task("clean windows", 20, "wash dishes")
        self.task_wash_dishes = Task("wash dishes", 10, "cook dinner")
        self.task_cook_dinner = Task("cook dinner", 60, "clean windows")
        # self.task_wash_clothes = Task("wash clothes", 45)
        # self.task_do_ironing = Task("do ironing", 35)
    
    def test_task_has_description(self):
        self.assertEqual("clean windows", self.task_clean_windows.description)

    def test_task_has_duration(self):
        self.assertEqual(20, self.task_clean_windows.duration)


    def test_cw_over_wd(self):
        self.assertEqual("clean windows", get_preferred_option(self.task_clean_windows, self.task_wash_dishes))

    def test_cw_over_wd_2(self):
        self.assertEqual("clean windows", get_preferred_option(self.task_wash_dishes, self.task_clean_windows))


    def test_cd_over_cw(self):
        self.assertEqual("cook dinner", get_preferred_option(self.task_clean_windows, self.task_cook_dinner))

    def test_wd_over_cd__1(self):
        self.assertEqual("wash dishes", get_preferred_option(self.task_wash_dishes, self.task_cook_dinner))
    
    def test_wd_over_cd__2(self):
        self.assertEqual("wash dishes", get_preferred_option(self.task_cook_dinner, self.task_wash_dishes))

    def test_returns_task_if_tasks_same(self):
        self.assertEqual("wash dishes", get_preferred_option(self.task_wash_dishes, self.task_wash_dishes))
    
    # -----------
    # Extension 
    
    # def test_wc_over_cw(self):
    #     self.assertEqual("wash clothes", get_preferred_option(self.task_clean_windows, self.task_wash_clothes))