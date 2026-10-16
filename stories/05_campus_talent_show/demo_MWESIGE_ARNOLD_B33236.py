from story import ShowClock


# extend() accepts positive minutes and leaves the clock unchanged otherwise.
print("=== MC GETS EXTRA TIME: NORMAL CASE ===")
normal_clock = ShowClock(8)
expected = "True; 11 minutes remaining"
actual = f"{normal_clock.extend(3)}; {normal_clock.remaining} minutes remaining"
print(f"Expected: {expected}")
print(f"Actual:   {actual}")

print("\n=== MC GETS EXTRA TIME: ZERO-MINUTE BOUNDARY ===")
zero_clock = ShowClock(8)
expected = "False; 8 minutes remaining"
actual = f"{zero_clock.extend(0)}; {zero_clock.remaining} minutes remaining"
print(f"Expected: {expected}")
print(f"Actual:   {actual}")

print("\n=== MC GETS EXTRA TIME: NEGATIVE INPUT ===")
negative_clock = ShowClock(8)
expected = "False; 8 minutes remaining"
actual = f"{negative_clock.extend(-2)}; {negative_clock.remaining} minutes remaining"
print(f"Expected: {expected}")
print(f"Actual:   {actual}")
