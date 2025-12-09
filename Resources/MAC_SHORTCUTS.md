# Mac Keyboard Shortcuts for Python in VSCode

**Your quick reference for coding on Mac**

---

## 🎹 Essential VSCode Shortcuts

| Action | Mac Shortcut |
|--------|--------------|
| **Run selected code** | `Shift + Return` |
| **Run entire file** | `Control + Option + N` |
| **Save file** | `Cmd + S` |
| **Save all files** | `Cmd + Option + S` |
| **Open/close terminal** | ``Control + ` `` (backtick) |
| **Comment/uncomment lines** | `Cmd + /` |
| **Open Command Palette** | `Cmd + Shift + P` |
| **Find in file** | `Cmd + F` |
| **Find in all files** | `Cmd + Shift + F` |
| **Split editor** | `Cmd + \` |
| **Close editor** | `Cmd + W` |
| **Undo** | `Cmd + Z` |
| **Redo** | `Cmd + Shift + Z` |
| **Select all** | `Cmd + A` |
| **Copy** | `Cmd + C` |
| **Paste** | `Cmd + V` |
| **Cut** | `Cmd + X` |
| **Duplicate line** | `Shift + Option + Down` |
| **Move line up/down** | `Option + Up/Down` |
| **Delete line** | `Cmd + Shift + K` |
| **Go to line** | `Control + G` |
| **Multi-cursor** | `Cmd + Click` |

---

## 💻 Terminal Commands (for Zsh/Bash)

### File & Directory Navigation
```bash
pwd                 # Print working directory (where am I?)
ls                  # List files in current directory
ls -la              # List all files with details
cd folder_name      # Change to a folder
cd ..               # Go up one folder
cd ~                # Go to home directory
```

### Running Python
```bash
python3 filename.py          # Run a Python file
python3 --version            # Check Python version
which python3                # Find where Python is installed
```

### Terminal Control
```bash
clear               # Clear the terminal screen
exit                # Exit Python interactive mode
Control + C         # Stop running program
Control + D         # Exit Python interactive shell
```

### File Operations (Use Tools Instead!)
```bash
# DON'T use these - use VSCode tools instead:
cat filename.py     # Use Read tool instead
nano filename.py    # Use Edit tool instead
```

---

## 🐍 Python Interactive Mode

### Enter Python Shell
```bash
python3             # Start Python interactive mode
```

You'll see `>>>` - now you can type Python code directly!

### Exit Python Shell
```python
exit()              # Type this and press Enter
# OR press Control + D
```

---

## ⚙️ VSCode Settings

### Open Settings
- `Cmd + ,` - Opens settings
- Search for what you need

### Useful Settings to Know
- **Auto Save**: Search "auto save" → Set to "afterDelay"
- **Font Size**: Search "font size" → Adjust to your preference
- **Tab Size**: Search "tab size" → Usually 4 for Python

---

## 🎯 Running Code: The Three Ways

### Method 1: Run Selection (Best for Practice Files)
1. Highlight the code you want to run
2. Press `Shift + Return`
3. Code runs in Python terminal

**When to use:** Individual exercises, testing snippets

---

### Method 2: Run Entire File
1. Click ▶️ button (top-right)
2. OR press `Control + Option + N`

**When to use:** Complete programs, no `input()` conflicts

---

### Method 3: Run in Terminal Manually
1. Open terminal: ``Control + ` ``
2. Type: `python3 filename.py`
3. Press `Return`

**When to use:** Rarely needed, mainly for troubleshooting

---

## 📁 File Management Shortcuts

| Action | Mac Shortcut |
|--------|--------------|
| **New file** | `Cmd + N` |
| **Open file** | `Cmd + O` |
| **Close file** | `Cmd + W` |
| **Switch between files** | `Control + Tab` |
| **Close all files** | `Cmd + K` then `Cmd + W` |
| **Show file explorer** | `Cmd + Shift + E` |
| **Quick file open** | `Cmd + P` |

---

## 🔍 Finding & Replacing

| Action | Mac Shortcut |
|--------|--------------|
| **Find** | `Cmd + F` |
| **Find next** | `Cmd + G` |
| **Find previous** | `Cmd + Shift + G` |
| **Replace** | `Cmd + Option + F` |
| **Find in all files** | `Cmd + Shift + F` |

---

## ✏️ Editing Shortcuts

| Action | Mac Shortcut |
|--------|--------------|
| **Select word** | `Cmd + D` |
| **Select all** | `Cmd + A` |
| **Select line** | `Cmd + L` |
| **Delete line** | `Cmd + Shift + K` |
| **Indent** | `Cmd + ]` |
| **Unindent** | `Cmd + [` |
| **Toggle comment** | `Cmd + /` |
| **Move line up** | `Option + Up` |
| **Move line down** | `Option + Down` |
| **Copy line up** | `Shift + Option + Up` |
| **Copy line down** | `Shift + Option + Down` |

---

## 🪟 Window & Panel Management

| Action | Mac Shortcut |
|--------|--------------|
| **Toggle sidebar** | `Cmd + B` |
| **Toggle terminal** | ``Control + ` `` |
| **Split editor** | `Cmd + \` |
| **Focus editor group** | `Cmd + 1/2/3` |
| **Zoom in** | `Cmd + =` |
| **Zoom out** | `Cmd + -` |
| **Full screen** | `Control + Cmd + F` |

---

## 🐛 Debugging

| Action | Mac Shortcut |
|--------|--------------|
| **Toggle breakpoint** | `F9` |
| **Start debugging** | `F5` |
| **Step over** | `F10` |
| **Step into** | `F11` |
| **Stop debugging** | `Shift + F5` |

---

## 💡 Pro Tips for Mac

### Difference Between Control and Cmd
- **Control (^)**: VSCode-specific shortcuts, terminal
- **Command (⌘)**: System-level, text editing, file operations

### Terminal Tips
- **Backtick key**: ``Control + ` `` (top-left of keyboard, under Esc)
- **Clear terminal**: Type `clear` and press Return
- **Stop program**: `Control + C` (not Cmd!)
- **Python is `python3`**: On Mac, always use `python3`, not `python`

### Common Confusion
- `Shift + Return` = Run selected Python code
- `Return` alone = New line
- In terminal after prompt, just type your answer and press `Return`

---

## 🎨 Customizing Your Setup

### Change Keyboard Shortcuts
1. `Cmd + K` then `Cmd + S` - Opens keyboard shortcuts
2. Search for the command
3. Click and set your preferred shortcut

### Mac System Settings That Help
1. Turn off "Add period with double-space"
   - System Settings → Keyboard → Uncheck that option

2. Enable key repeat
   - System Settings → Keyboard → Key repeat rate (faster)

---

## 🚀 Workflow Tips

### Starting a Coding Session
1. `Cmd + O` - Open your practice file
2. ``Control + ` `` - Open terminal
3. `Cmd + \` - Split view (lesson on left, practice on right)
4. Start coding!

### During Practice
1. Write code in editor
2. Highlight code
3. `Shift + Return` - Run it
4. Check output in terminal below

### When Things Go Wrong
1. ``Control + ` `` - Check terminal for errors
2. Read error message (last line most important!)
3. Click trash icon on Python terminal
4. Run code fresh

---

## 📝 Most Important to Remember

**For Running Code:**
- `Shift + Return` - Your best friend for practice
- ``Control + ` `` - Open/close terminal

**For Editing:**
- `Cmd + S` - Save (do this often!)
- `Cmd + /` - Comment out code quickly

**For Terminal:**
- `clear` - Clean terminal screen
- `Control + C` - Stop running program
- `exit()` - Exit Python shell

---

**Print this and keep it by your keyboard!**
