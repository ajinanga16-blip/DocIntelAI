class ComplianceStyleMapper:

    STYLE_MAP = {

        "Microsoft Technical Writing":
        "Microsoft Test",

        "Google Developer Documentation":
        "Google Test",

        "IBM Technical Documentation":
        None,

        "Chicago Editorial Style":
        None
    }

    def get_compliance_profile(
        self,
        style_name
    ):

        return self.STYLE_MAP.get(
            style_name
        )