from user import User


class UserService:
    _uri: str

    def __init__(self, uri) -> None:
        self._uri = uri

    def get_users(self):
        return [
            User(id=932210, login="lsilva", given_name="Leroy", surname="Silva"),
            User(id=932211, login="lguerrero", given_name="Lynn", surname="Guerrero"),
            User(id=932212, login="mshort", given_name="Mary", surname="Short"),
            User(id=932213, login="sgonzalez", given_name="Sandra", surname="Gonzalez"),
            User(id=932214, login="mfrench", given_name="Max", surname="French"),
            User(id=932215, login="smccarthy", given_name="Sharon", surname="Mccarthy"),
            User(id=932216, login="chiggins", given_name="Clara", surname="Higgins"),
            User(id=932217, login="bbenson", given_name="Betty", surname="Benson"),
            User(id=932218, login="msilva", given_name="Michelle", surname="Silva"),
            User(id=932219, login="hbenson", given_name="Helen", surname="Benson"),
            User(id=932220, login="afrank", given_name="Angela", surname="Frank"),
            User(id=932221, login="mjuarez", given_name="Matthew", surname="Juarez"),
            User(id=932222, login="mtorres", given_name="Melody", surname="Torres"),
            User(id=932223, login="swaters", given_name="Sandra", surname="Waters"),
            User(id=932224, login="shansen", given_name="Shelly", surname="Hansen"),
            User(id=932225, login="lrivera", given_name="Leon", surname="Rivera"),
            User(
                id=932226, login="echristian", given_name="Eduardo", surname="Christian"
            ),
            User(id=932227, login="ebaxter", given_name="Erik", surname="Baxter"),
            User(
                id=932228, login="bmccarthy", given_name="Blanche", surname="Mccarthy"
            ),
            User(
                id=932229,
                login="cmaldonado",
                given_name="Christian",
                surname="Maldonado",
            ),
            User(id=932230, login="mwalters", given_name="Matthew", surname="Walters"),
            User(
                id=932231, login="ahernandez", given_name="Angela", surname="Hernandez"
            ),
            User(id=932232, login="lsherman", given_name="Leon", surname="Sherman"),
            User(id=932233, login="rmckenzie", given_name="Roland", surname="Mckenzie"),
            User(id=932234, login="cmckenzie", given_name="Carlos", surname="Mckenzie"),
            User(id=932235, login="keverett", given_name="Kirk", surname="Everett"),
            User(id=932236, login="mlee", given_name="Mary", surname="Lee"),
            User(
                id=932237, login="cbartlett", given_name="Christian", surname="Bartlett"
            ),
            User(id=932238, login="ashort", given_name="Antonio", surname="Short"),
            User(id=932239, login="arobbins", given_name="Arthur", surname="Robbins"),
            User(id=192110, login="lsilva", given_name="Leroy", surname="Silva"),
            User(id=192111, login="lguerrero", given_name="Lynn", surname="Guerrero"),
            User(id=192112, login="mshort", given_name="Mary", surname="Short"),
            User(id=192113, login="sgonzalez", given_name="Sandra", surname="Gonzalez"),
            User(id=192114, login="mfrench", given_name="Max", surname="French"),
            User(id=192115, login="smccarthy", given_name="Sharon", surname="Mccarthy"),
            User(id=192116, login="chiggins", given_name="Clara", surname="Higgins"),
            User(id=192117, login="bbenson", given_name="Betty", surname="Benson"),
            User(id=192118, login="msilva", given_name="Michelle", surname="Silva"),
            User(id=192119, login="hbenson", given_name="Helen", surname="Benson"),
            User(id=192120, login="afrank", given_name="Angela", surname="Frank"),
            User(id=192121, login="mjuarez", given_name="Matthew", surname="Juarez"),
            User(id=192122, login="mtorres", given_name="Melody", surname="Torres"),
            User(id=192123, login="swaters", given_name="Sandra", surname="Waters"),
            User(id=192124, login="shansen", given_name="Shelly", surname="Hansen"),
            User(id=192125, login="lrivera", given_name="Leon", surname="Rivera"),
            User(
                id=192126, login="echristian", given_name="Eduardo", surname="Christian"
            ),
            User(id=192127, login="ebaxter", given_name="Erik", surname="Baxter"),
            User(
                id=192128, login="bmccarthy", given_name="Blanche", surname="Mccarthy"
            ),
            User(
                id=192129,
                login="cmaldonado",
                given_name="Christian",
                surname="Maldonado",
            ),
            User(id=192130, login="mwalters", given_name="Matthew", surname="Walters"),
            User(
                id=192131, login="ahernandez", given_name="Angela", surname="Hernandez"
            ),
            User(id=192132, login="lsherman", given_name="Leon", surname="Sherman"),
            User(id=192133, login="rmckenzie", given_name="Roland", surname="Mckenzie"),
            User(id=192134, login="cmckenzie", given_name="Carlos", surname="Mckenzie"),
            User(id=192135, login="keverett", given_name="Kirk", surname="Everett"),
            User(id=192136, login="mlee", given_name="Mary", surname="Lee"),
            User(
                id=192137, login="cbartlett", given_name="Christian", surname="Bartlett"
            ),
            User(id=192138, login="ashort", given_name="Antonio", surname="Short"),
            User(id=192139, login="arobbins", given_name="Arthur", surname="Robbins"),
            User(id=1932210, login="lsilva", given_name="Leroy", surname="Silva"),
            User(id=1932211, login="lguerrero", given_name="Lynn", surname="Guerrero"),
            User(id=1932212, login="mshort", given_name="Mary", surname="Short"),
            User(
                id=1932213, login="sgonzalez", given_name="Sandra", surname="Gonzalez"
            ),
            User(id=1932214, login="mfrench", given_name="Max", surname="French"),
            User(
                id=1932215, login="smccarthy", given_name="Sharon", surname="Mccarthy"
            ),
            User(id=1932216, login="chiggins", given_name="Clara", surname="Higgins"),
            User(id=1932217, login="bbenson", given_name="Betty", surname="Benson"),
            User(id=1932218, login="msilva", given_name="Michelle", surname="Silva"),
            User(id=1932219, login="hbenson", given_name="Helen", surname="Benson"),
            User(id=1932220, login="afrank", given_name="Angela", surname="Frank"),
            User(id=1932221, login="mjuarez", given_name="Matthew", surname="Juarez"),
            User(id=1932222, login="mtorres", given_name="Melody", surname="Torres"),
            User(id=1932223, login="swaters", given_name="Sandra", surname="Waters"),
            User(id=1932224, login="shansen", given_name="Shelly", surname="Hansen"),
            User(id=1932225, login="lrivera", given_name="Leon", surname="Rivera"),
            User(
                id=1932226,
                login="echristian",
                given_name="Eduardo",
                surname="Christian",
            ),
            User(id=1932227, login="ebaxter", given_name="Erik", surname="Baxter"),
            User(
                id=1932228, login="bmccarthy", given_name="Blanche", surname="Mccarthy"
            ),
            User(
                id=1932229,
                login="cmaldonado",
                given_name="Christian",
                surname="Maldonado",
            ),
            User(id=1932230, login="mwalters", given_name="Matthew", surname="Walters"),
            User(
                id=1932231, login="ahernandez", given_name="Angela", surname="Hernandez"
            ),
            User(id=1932232, login="lsherman", given_name="Leon", surname="Sherman"),
            User(
                id=1932233, login="rmckenzie", given_name="Roland", surname="Mckenzie"
            ),
            User(
                id=1932234, login="cmckenzie", given_name="Carlos", surname="Mckenzie"
            ),
            User(id=1932235, login="keverett", given_name="Kirk", surname="Everett"),
            User(id=1932236, login="mlee", given_name="Mary", surname="Lee"),
            User(
                id=1932237,
                login="cbartlett",
                given_name="Christian",
                surname="Bartlett",
            ),
            User(id=1932238, login="ashort", given_name="Antonio", surname="Short"),
            User(id=1932239, login="arobbins", given_name="Arthur", surname="Robbins"),
            User(id=1192110, login="lsilva", given_name="Leroy", surname="Silva"),
            User(id=1192111, login="lguerrero", given_name="Lynn", surname="Guerrero"),
            User(id=1192112, login="mshort", given_name="Mary", surname="Short"),
            User(
                id=1192113, login="sgonzalez", given_name="Sandra", surname="Gonzalez"
            ),
            User(id=1192114, login="mfrench", given_name="Max", surname="French"),
            User(
                id=1192115, login="smccarthy", given_name="Sharon", surname="Mccarthy"
            ),
            User(id=1192116, login="chiggins", given_name="Clara", surname="Higgins"),
            User(id=1192117, login="bbenson", given_name="Betty", surname="Benson"),
            User(id=1192118, login="msilva", given_name="Michelle", surname="Silva"),
            User(id=1192119, login="hbenson", given_name="Helen", surname="Benson"),
            User(id=1192120, login="afrank", given_name="Angela", surname="Frank"),
            User(id=1192121, login="mjuarez", given_name="Matthew", surname="Juarez"),
            User(id=1192122, login="mtorres", given_name="Melody", surname="Torres"),
            User(id=1192123, login="swaters", given_name="Sandra", surname="Waters"),
            User(id=1192124, login="shansen", given_name="Shelly", surname="Hansen"),
            User(id=1192125, login="lrivera", given_name="Leon", surname="Rivera"),
            User(
                id=1192126,
                login="echristian",
                given_name="Eduardo",
                surname="Christian",
            ),
            User(id=1192127, login="ebaxter", given_name="Erik", surname="Baxter"),
            User(
                id=1192128, login="bmccarthy", given_name="Blanche", surname="Mccarthy"
            ),
            User(
                id=1192129,
                login="cmaldonado",
                given_name="Christian",
                surname="Maldonado",
            ),
            User(id=1192130, login="mwalters", given_name="Matthew", surname="Walters"),
            User(
                id=1192131, login="ahernandez", given_name="Angela", surname="Hernandez"
            ),
            User(id=1192132, login="lsherman", given_name="Leon", surname="Sherman"),
            User(
                id=1192133, login="rmckenzie", given_name="Roland", surname="Mckenzie"
            ),
            User(
                id=1192134, login="cmckenzie", given_name="Carlos", surname="Mckenzie"
            ),
            User(id=1192135, login="keverett", given_name="Kirk", surname="Everett"),
            User(id=1192136, login="mlee", given_name="Mary", surname="Lee"),
            User(
                id=1192137,
                login="cbartlett",
                given_name="Christian",
                surname="Bartlett",
            ),
            User(id=1192138, login="ashort", given_name="Antonio", surname="Short"),
            User(id=1192139, login="arobbins", given_name="Arthur", surname="Robbins"),
            User(id=2932210, login="lsilva", given_name="Leroy", surname="Silva"),
            User(id=2932211, login="lguerrero", given_name="Lynn", surname="Guerrero"),
            User(id=2932212, login="mshort", given_name="Mary", surname="Short"),
            User(
                id=2932213, login="sgonzalez", given_name="Sandra", surname="Gonzalez"
            ),
            User(id=2932214, login="mfrench", given_name="Max", surname="French"),
            User(
                id=2932215, login="smccarthy", given_name="Sharon", surname="Mccarthy"
            ),
            User(id=2932216, login="chiggins", given_name="Clara", surname="Higgins"),
            User(id=2932217, login="bbenson", given_name="Betty", surname="Benson"),
            User(id=2932218, login="msilva", given_name="Michelle", surname="Silva"),
            User(id=2932219, login="hbenson", given_name="Helen", surname="Benson"),
            User(id=2932220, login="afrank", given_name="Angela", surname="Frank"),
            User(id=2932221, login="mjuarez", given_name="Matthew", surname="Juarez"),
            User(id=2932222, login="mtorres", given_name="Melody", surname="Torres"),
            User(id=2932223, login="swaters", given_name="Sandra", surname="Waters"),
            User(id=2932224, login="shansen", given_name="Shelly", surname="Hansen"),
            User(id=2932225, login="lrivera", given_name="Leon", surname="Rivera"),
            User(
                id=2932226,
                login="echristian",
                given_name="Eduardo",
                surname="Christian",
            ),
            User(id=2932227, login="ebaxter", given_name="Erik", surname="Baxter"),
            User(
                id=2932228, login="bmccarthy", given_name="Blanche", surname="Mccarthy"
            ),
            User(
                id=2932229,
                login="cmaldonado",
                given_name="Christian",
                surname="Maldonado",
            ),
            User(id=2932230, login="mwalters", given_name="Matthew", surname="Walters"),
            User(
                id=2932231, login="ahernandez", given_name="Angela", surname="Hernandez"
            ),
            User(id=2932232, login="lsherman", given_name="Leon", surname="Sherman"),
            User(
                id=2932233, login="rmckenzie", given_name="Roland", surname="Mckenzie"
            ),
            User(
                id=2932234, login="cmckenzie", given_name="Carlos", surname="Mckenzie"
            ),
            User(id=2932235, login="keverett", given_name="Kirk", surname="Everett"),
            User(id=2932236, login="mlee", given_name="Mary", surname="Lee"),
            User(
                id=2932237,
                login="cbartlett",
                given_name="Christian",
                surname="Bartlett",
            ),
            User(id=2932238, login="ashort", given_name="Antonio", surname="Short"),
            User(id=2932239, login="arobbins", given_name="Arthur", surname="Robbins"),
            User(id=2192110, login="lsilva", given_name="Leroy", surname="Silva"),
            User(id=2192111, login="lguerrero", given_name="Lynn", surname="Guerrero"),
            User(id=2192112, login="mshort", given_name="Mary", surname="Short"),
            User(
                id=2192113, login="sgonzalez", given_name="Sandra", surname="Gonzalez"
            ),
            User(id=2192114, login="mfrench", given_name="Max", surname="French"),
            User(
                id=2192115, login="smccarthy", given_name="Sharon", surname="Mccarthy"
            ),
            User(id=2192116, login="chiggins", given_name="Clara", surname="Higgins"),
            User(id=2192117, login="bbenson", given_name="Betty", surname="Benson"),
            User(id=2192118, login="msilva", given_name="Michelle", surname="Silva"),
            User(id=2192119, login="hbenson", given_name="Helen", surname="Benson"),
            User(id=2192120, login="afrank", given_name="Angela", surname="Frank"),
            User(id=2192121, login="mjuarez", given_name="Matthew", surname="Juarez"),
            User(id=2192122, login="mtorres", given_name="Melody", surname="Torres"),
            User(id=2192123, login="swaters", given_name="Sandra", surname="Waters"),
            User(id=2192124, login="shansen", given_name="Shelly", surname="Hansen"),
            User(id=2192125, login="lrivera", given_name="Leon", surname="Rivera"),
            User(
                id=2192126,
                login="echristian",
                given_name="Eduardo",
                surname="Christian",
            ),
            User(id=2192127, login="ebaxter", given_name="Erik", surname="Baxter"),
            User(
                id=2192128, login="bmccarthy", given_name="Blanche", surname="Mccarthy"
            ),
            User(
                id=2192129,
                login="cmaldonado",
                given_name="Christian",
                surname="Maldonado",
            ),
            User(id=2192130, login="mwalters", given_name="Matthew", surname="Walters"),
            User(
                id=2192131, login="ahernandez", given_name="Angela", surname="Hernandez"
            ),
            User(id=2192132, login="lsherman", given_name="Leon", surname="Sherman"),
            User(
                id=2192133, login="rmckenzie", given_name="Roland", surname="Mckenzie"
            ),
            User(
                id=2192134, login="cmckenzie", given_name="Carlos", surname="Mckenzie"
            ),
            User(id=2192135, login="keverett", given_name="Kirk", surname="Everett"),
            User(id=2192136, login="mlee", given_name="Mary", surname="Lee"),
            User(
                id=2192137,
                login="cbartlett",
                given_name="Christian",
                surname="Bartlett",
            ),
            User(id=2192138, login="ashort", given_name="Antonio", surname="Short"),
            User(id=2192139, login="arobbins", given_name="Arthur", surname="Robbins"),
            User(id=21932210, login="lsilva", given_name="Leroy", surname="Silva"),
            User(id=21932211, login="lguerrero", given_name="Lynn", surname="Guerrero"),
            User(id=21932212, login="mshort", given_name="Mary", surname="Short"),
            User(
                id=21932213, login="sgonzalez", given_name="Sandra", surname="Gonzalez"
            ),
            User(id=21932214, login="mfrench", given_name="Max", surname="French"),
            User(
                id=21932215, login="smccarthy", given_name="Sharon", surname="Mccarthy"
            ),
            User(id=21932216, login="chiggins", given_name="Clara", surname="Higgins"),
            User(id=21932217, login="bbenson", given_name="Betty", surname="Benson"),
            User(id=21932218, login="msilva", given_name="Michelle", surname="Silva"),
            User(id=21932219, login="hbenson", given_name="Helen", surname="Benson"),
            User(id=21932220, login="afrank", given_name="Angela", surname="Frank"),
            User(id=21932221, login="mjuarez", given_name="Matthew", surname="Juarez"),
            User(id=21932222, login="mtorres", given_name="Melody", surname="Torres"),
            User(id=21932223, login="swaters", given_name="Sandra", surname="Waters"),
            User(id=21932224, login="shansen", given_name="Shelly", surname="Hansen"),
            User(id=21932225, login="lrivera", given_name="Leon", surname="Rivera"),
            User(
                id=21932226,
                login="echristian",
                given_name="Eduardo",
                surname="Christian",
            ),
            User(id=21932227, login="ebaxter", given_name="Erik", surname="Baxter"),
            User(
                id=21932228, login="bmccarthy", given_name="Blanche", surname="Mccarthy"
            ),
            User(
                id=21932229,
                login="cmaldonado",
                given_name="Christian",
                surname="Maldonado",
            ),
            User(
                id=21932230, login="mwalters", given_name="Matthew", surname="Walters"
            ),
            User(
                id=21932231,
                login="ahernandez",
                given_name="Angela",
                surname="Hernandez",
            ),
            User(id=21932232, login="lsherman", given_name="Leon", surname="Sherman"),
            User(
                id=21932233, login="rmckenzie", given_name="Roland", surname="Mckenzie"
            ),
            User(
                id=21932234, login="cmckenzie", given_name="Carlos", surname="Mckenzie"
            ),
            User(id=21932235, login="keverett", given_name="Kirk", surname="Everett"),
            User(id=21932236, login="mlee", given_name="Mary", surname="Lee"),
            User(
                id=21932237,
                login="cbartlett",
                given_name="Christian",
                surname="Bartlett",
            ),
            User(id=21932238, login="ashort", given_name="Antonio", surname="Short"),
            User(id=21932239, login="arobbins", given_name="Arthur", surname="Robbins"),
            User(id=21192110, login="lsilva", given_name="Leroy", surname="Silva"),
            User(id=21192111, login="lguerrero", given_name="Lynn", surname="Guerrero"),
            User(id=21192112, login="mshort", given_name="Mary", surname="Short"),
            User(
                id=21192113, login="sgonzalez", given_name="Sandra", surname="Gonzalez"
            ),
            User(id=21192114, login="mfrench", given_name="Max", surname="French"),
            User(
                id=21192115, login="smccarthy", given_name="Sharon", surname="Mccarthy"
            ),
            User(id=21192116, login="chiggins", given_name="Clara", surname="Higgins"),
            User(id=21192117, login="bbenson", given_name="Betty", surname="Benson"),
            User(id=21192118, login="msilva", given_name="Michelle", surname="Silva"),
            User(id=21192119, login="hbenson", given_name="Helen", surname="Benson"),
            User(id=21192120, login="afrank", given_name="Angela", surname="Frank"),
            User(id=21192121, login="mjuarez", given_name="Matthew", surname="Juarez"),
            User(id=21192122, login="mtorres", given_name="Melody", surname="Torres"),
            User(id=21192123, login="swaters", given_name="Sandra", surname="Waters"),
            User(id=21192124, login="shansen", given_name="Shelly", surname="Hansen"),
            User(id=21192125, login="lrivera", given_name="Leon", surname="Rivera"),
            User(
                id=21192126,
                login="echristian",
                given_name="Eduardo",
                surname="Christian",
            ),
            User(id=21192127, login="ebaxter", given_name="Erik", surname="Baxter"),
            User(
                id=21192128, login="bmccarthy", given_name="Blanche", surname="Mccarthy"
            ),
            User(
                id=21192129,
                login="cmaldonado",
                given_name="Christian",
                surname="Maldonado",
            ),
            User(
                id=21192130, login="mwalters", given_name="Matthew", surname="Walters"
            ),
            User(
                id=21192131,
                login="ahernandez",
                given_name="Angela",
                surname="Hernandez",
            ),
            User(id=21192132, login="lsherman", given_name="Leon", surname="Sherman"),
            User(
                id=21192133, login="rmckenzie", given_name="Roland", surname="Mckenzie"
            ),
            User(
                id=21192134, login="cmckenzie", given_name="Carlos", surname="Mckenzie"
            ),
            User(id=21192135, login="keverett", given_name="Kirk", surname="Everett"),
            User(id=21192136, login="mlee", given_name="Mary", surname="Lee"),
            User(
                id=21192137,
                login="cbartlett",
                given_name="Christian",
                surname="Bartlett",
            ),
            User(id=21192138, login="ashort", given_name="Antonio", surname="Short"),
            User(id=21192139, login="arobbins", given_name="Arthur", surname="Robbins"),
        ]
