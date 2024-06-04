import os


class Path:
    project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    common_path = project_path + os.sep + "common"

    config_path = project_path + os.sep + "config"

    log_path = project_path + os.sep + "log"

    report_path = project_path + os.sep + "report"

    setting_path = project_path + os.path.sep + "setting"

    config_file_path = project_path + os.path.sep + "testdata" + os.path.sep + "config.yaml"

    test_file_path = project_path + os.path.sep + "testdata" + os.path.sep + "test_pc_add.yaml"

    test_pda_path = project_path + os.path.sep + "testdata" + os.path.sep + "test_pda_banding.yaml"

    data_path = project_path + os.path.sep + "testdata"

    util_path = project_path + os.path.sep + "utils"
