class Party:
    def __init__(self, id):
        self.id = id
        self.seed_s = {"0": "", "1": ""}
        self.seed_s_tmp = {"0": "", "1": ""}
        self.seed_t = {"0": "", "1": ""}
        self.seed_t_tmp = {"0": "", "1": ""}
        self.st = ""
        self.st_divide = {
            "s": {
                "0": "",
                "1": "",
            },
            "t": {
                "0": "",
                "1": "",
            }
        }
        self.cw_list = []
