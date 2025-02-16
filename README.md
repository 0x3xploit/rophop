# ROPHOP - ROP Gadget Finder

ROP (Return-Oriented Programming) gadget finder designed for the OSED exam. This tool filters the output from [RP++](https://github.com/0vercl0k/rp) and categorizes useful gadgets such as `pop`, `add`, `jmp`, `xor`, `mov`, `neg`, and `xchg` for exploit development.

## Features
- Extracts and categorizes specific ROP gadgets
- Supports filtering gadgets from RP++ output
- Displays categorized gadgets in a structured format with colors

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/0x3xploit/rophop.git
   cd rophop
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script with an RP++ output file:
```bash
python3 rophop.py <filename.txt>
```

### Example Output
```
├── Found 3 PR gadgets
│   ├──>  0x123456: pop eax; ret;
│   ├──>  0x654321: pop ebx; ret;
...
├── Found 2 ADD gadgets
│   ├──>  0x789abc: add eax, ebx; ret;
```

## Supported Gadgets
- `PR`  - Pop Register (`pop reg; ret;`)
- `PPR` - Pop-Pop-Ret (`pop reg; pop reg; ret;`)
- `ADD` - Add (`add reg, val; ret;`)
- `JMP` - Jump (`jmp reg;`)
- `XOR` - XOR (`xor reg, reg; ret;`)
- `MOV` - Move (`mov reg, val; ret;`)
- `NEG` - Negate (`neg reg; ret;`)
- `XCHG` - Exchange (`xchg reg, reg; ret;`)

## Notes
- This tool is optimized for OSED exploit development.
- The tool is under active development, and new features may be added.



