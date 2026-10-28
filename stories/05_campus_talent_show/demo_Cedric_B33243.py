"""Demonstrate value semantics, validation, and a side-effect-free preview."""
from story import Dance, StageTime, TalentShow, ThankYouSpeech, audition


def main():
    speech = ThankYouSpeech()
    print("Expected audition: dance and thank-you speech descriptions.")
    audition([Dance("Mukono Movers"), speech])

    normal_show = TalentShow("Cedric", 1)
    print("Expected normal booking: booked; 0 minutes left; 1 booked act.")
    print(f"Actual: {normal_show.book(speech)}")
    print(f"Actual state: {normal_show.clock.remaining} minutes left; "
          f"booked acts: {normal_show.act_count}.")

    empty_show = TalentShow("Cedric", 0)
    print("Expected boundary case: refused; 0 minutes left; 0 booked acts.")
    print(f"Actual: {empty_show.book(speech)}")
    print(f"Actual state: {empty_show.clock.remaining} minutes left; "
          f"booked acts: {empty_show.act_count}.")

    three_thousand = StageTime(3000)
    another_three_thousand = StageTime(3000)
    five_hundred = StageTime(500)
    total = three_thousand + five_hundred
    print(f"Display: {three_thousand}")
    print(f"Developer: {three_thousand!r}")
    print(f"Equal: {three_thousand == another_three_thousand}; "
          f"unequal: {three_thousand != five_hundred}")
    print(f"Addition: {total}; operands unchanged: "
          f"{three_thousand.amount == 3000 and five_hundred.amount == 500}")

    try:
        three_thousand.amount = 99
    except AttributeError as error:
        print(f"Read-only amount: refused ({error})")

    print(f"Unsupported equality: {StageTime.__eq__(three_thousand, 3000) is NotImplemented}")
    print(f"Unsupported addition: {StageTime.__add__(three_thousand, 3000) is NotImplemented}")

    invalid_values = (-1, 1.5, True)
    for invalid in invalid_values:
        try:
            StageTime(invalid)
        except (TypeError, ValueError) as error:
            print(f"Invalid {invalid!r}: {error}")

    preview_show = TalentShow("Cedric", 20)
    choices = [Dance("Mukono Movers", 6), ThankYouSpeech(), 300]

    class TimedChoice:
        def duration(self):
            return 4

    choices[2] = TimedChoice()
    print(f"Preview: {preview_show.preview_total(choices)}")
    print(f"Preview state: {preview_show.clock.remaining} minutes left; "
          f"{preview_show.act_count} booked acts")
    print(f"Empty preview: {preview_show.preview_total([])}")


if __name__ == "__main__":
    main()
