import re
import sys
import os
from colorama import Fore, Style

not_found = {
    "PR": False,
    "PPR": False,
    "ADD": False,
    "JMP": False,
    "XOR": False,
    "MOV": False,
    "NEG": False,
    "XCHG": False
}

def display(count, gadgets, gadget_type):
    print("├── "+Fore.GREEN+f"Found {count} {gadget_type} gadgets"+Style.RESET_ALL)
    for gadget in gadgets:
        print("│\t├──>  ",end='')
        print(Fore.BLUE+f" {gadget.replace('; (1 found)', '')}"+Style.RESET_ALL, end='')

def snipper(gadget_type, regex, filename):
    with open(filename) as file:
        gadgets = []
        count = 0
        for line in file:
            if re.match(regex, line):
                count += 1
                gadgets.append(line)
        if count<=0:
            not_found[gadget_type] = True
        else:
            display(count, gadgets, gadget_type)

tags = {
    "PR":  r"0x[0-9a-fA-F]+:\s+pop\s+\w+\s*;\s*ret\s*;\s*\(1 found\)",
    "PPR": r"0x[0-9a-fA-F]+:\s+pop\s+\w+\s*;\s+pop\s+\w+\s*;\s*ret\s*;\s*\(1 found\)",
    "ADD": r"0x[0-9a-fA-F]+:\s+add\s+(?:al|ah|ax|eax|rax|bl|bh|bx|ebx|rbx|cl|ch|cx|ecx|rcx|dl|dh|dx|edx|rdx|sil|esi|rsi|dil|edi|rdi|bpl|ebp|rbp|spl|esp|rsp|r8|r9|r10|r11|r12|r13|r14|r15)\s*,\s*(?:\w+|0x[0-9a-fA-F]+)\s*;\s*ret\s*;\s*\(1 found\)",
    "JMP": r"0x[0-9a-fA-F]+:\s+jmp\s+\w+\s*;\s*\(1 found\)",
    "XOR": r"0x[0-9a-fA-F]+:\s+xor\s+\w+,\s*\w+\s*;\s*ret\s*;\s*\(1 found\)",
    "MOV": r"0x[0-9a-fA-F]+:\s+mov\s+(?:al|ah|ax|eax|rax|bl|bh|bx|ebx|rbx|cl|ch|cx|ecx|rcx|dl|dh|dx|edx|rdx|sil|esi|rsi|dil|edi|rdi|bpl|ebp|rbp|spl|esp|rsp|r8|r9|r10|r11|r12|r13|r14|r15)\s*,\s*(?:\w+|0x[0-9a-fA-F]+)\s*;\s*ret\s*;\s*\(1 found\)",
    "NEG": r"0x[0-9a-fA-F]+:\s+neg\s+\w+\s*;\s*ret\s*;\s*\(1 found\)",
    "XCHG": r"0x[0-9a-fA-F]+:\s+xchg\s+\w+\s*,\s*\w+\s*;\s*ret\s*;\s*\(1 found\)"
}

if __name__ == "__main__":
    if len(sys.argv)<2:
        print("Usage: python3 rophop.py <filename.txt>")
        sys.exit(1)
    filename = sys.argv[1]
    if not os.path.exists(filename):
        print(f"File not found {filename}")
        sys.exit(1)
    for gadget_type, regex in tags.items():
        snipper(gadget_type, regex, filename)
    for gadget_type, status in not_found.items():
        if status:
            print("├── "+Fore.RED+f"Found 0 {gadget_type}"+Style.RESET_ALL)

