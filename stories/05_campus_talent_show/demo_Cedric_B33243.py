"""Demonstrate the ThankYouSpeech extension with normal and refused bookings."""
from story import Dance, TalentShow, ThankYouSpeech, audition


def main():
	speech = ThankYouSpeech()
	print("Expected audition: dance and thank-you speech descriptions.")
	audition([Dance("Mukono Movers"), speech])

	# A one-minute show is the normal booking case for this one-minute act.
	normal_show = TalentShow("Cedric", 1)
	print("Expected normal booking: booked; 0 minutes left; 1 booked act.")
	print(f"Actual: {normal_show.book(speech)}")
	print(f"Actual state: {normal_show.clock.remaining} minutes left; "
		  f"booked acts: {normal_show.act_count}.")

	# A separate empty show checks that an unavailable slot is refused.
	empty_show = TalentShow("Cedric", 0)
	print("Expected boundary case: refused; 0 minutes left; 0 booked acts.")
	print(f"Actual: {empty_show.book(speech)}")
	print(f"Actual state: {empty_show.clock.remaining} minutes left; "
		  f"booked acts: {empty_show.act_count}.")


if __name__ == "__main__":
	main()
