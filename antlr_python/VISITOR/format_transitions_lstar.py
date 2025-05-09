from collections import defaultdict
import re

with open("abc.jff", "r") as f:
    data = f.read()


def get_state_information(states):
    dct = {}
    for state in states:
        final = False
        idx = re.findall('id="(.*?)"', state)
        name = re.findall('name="(.*?)"', state)
        x = re.findall("<x>(.*?)</x>", state)
        y = re.findall("<y>(.*?)</y>", state)
        if re.findall("<final/>", state):
            final = True
        dct[name[0]] = final
    return dct


def get_transitions(transitions):
    dct = defaultdict(dict)
    for transition in transitions:
        src = re.findall("<from>(.*?)</from>", transition)[0]
        dst = re.findall("<to>(.*?)</to>", transition)[0]
        read = re.findall("<read>(.*?)</read>", transition)[0]

        src = f"q{src}"
        r = f"{read}"
        dst = f"q{dst}"
        dct[src].update({r: dst})
    return dct


transitions = re.findall("<transition>.*?</transition>", data, re.DOTALL)
states = re.findall("<state.*?</state>", data, re.DOTALL)
st = get_state_information(states)
dct = get_transitions(transitions)
output = {}
for k, v in dct.items():
    output.update({k: (st.get(k, False), v)})
print(output)
