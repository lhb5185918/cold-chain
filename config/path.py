import os


class Path:
    project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    common_path = project_path + os.sep + "common"

    config_path = project_path + os.sep + "config"

    log_path = project_path + os.sep + "log"

    report_path = project_path + os.sep + "report"

    setting_path = project_path + os.path.sep + "setting"

    config_file_path = project_path + os.path.sep + "testdata" + os.path.sep + "config.yaml"

    base_data_path = project_path + os.path.sep + "testdata" + os.path.sep + "base_data.yaml"

    in_order_path = project_path + os.path.sep + "testdata" + os.path.sep + "in_order.yaml"

    data_path = project_path + os.path.sep + "testdata"

    util_path = project_path + os.path.sep + "utils"
