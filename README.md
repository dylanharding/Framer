# 🖼️ Framer!
*Take the guesswork out of your artwork!*

Ever made a wrong cut because your brain decided math was optional that day? Me too. That’s why I built **Framer** — a no-nonsense Python script that lets you *see* what your framed masterpiece will actually look like **before** you pick up the mat cutter and ruin a perfectly good Sunday.

But wait — there's more!

This isn’t just some boring static plot. Framer draws your frame **live** using Python’s good ol’ `turtle` module. That’s right — sit back and watch your art take shape, stroke by glorious stroke. It’s slow art, but on purpose.

---

## ✂️ What It Does  
You give it:
- Your art’s width and height  
- Your desired mat overlaps and side widths  
- Frame and rabbet sizes  

And it gives you:
- A mesmerizing animated drawing of your final framed piece  
- All calculated dimensions (inner/outer mat and frame)  
- A built-in **1/16" tolerance** so your art fits like a glove, not a cram

---

## 🧠 Why?
Because:
- Mental math is a trap  
- Visualization prevents heartbreak  
- Watching `turtle` draw rectangles is deeply therapeutic  

---

## ▶️ How to Use
1. Clone this repo  
2. Run the script:
   ```bash
   python framer.py
   ```
3. Enter your measurements in **inches using decimals**  
   > 📏 *Use `1.625` instead of `1 5/8` – fractions aren't accepted.*  
4. Watch as your custom frame gets lovingly hand-drawn on screen, like a Bob Ross for rectangles  
5. Get all your dimensions printed in the console. No guessing. No regrets.

---

## 📦 Requirements
- Python 3.x  
- No extra libraries — just you, the turtle, and the frame

---

## 🪛 Built-In Features
- Frame tolerance of **1/16" (0.0625")** built in for a snug fit around mat/glass  
- Custom top, bottom, and side mat widths supported  
- Input validation for smooth operation and fewer rage-quits

---

## 🐢 Having Trouble on Mac?

If you're on macOS and nothing appears when the turtle window should open, your Python installation might be missing `tkinter`, which `turtle` depends on.

To test:
```bash
python3 -m tkinter
```

If it errors out, reinstall Python from [python.org](https://www.python.org/downloads/) or use a version that includes GUI support (Homebrew versions may not!).

---

## 💬 Final Words  
This script won’t hang your art for you, but it *will* save your mat board, your wallet, and your weekend.  
Bonus: It’s weirdly satisfying to watch a turtle draw rectangles for 90 seconds.

Give it a spin. Your walls (and future self) will thank you.

