import os

from lib.helpers import ordinal_rank_percentile


class Donors:
	""" The donor list (a.k.a. Donors) holds a list of all donors, implemented as a dictionary.  The donor list has a way to identify whether or not somebody is a repeat donor. """
	def __init__(self):
		self.donors = dict()

	def add(self, donor_id, year):
		""" add to donor list """
		# Only add them if they aren't already in the list.  (Because if they are already in the list, we don't want to overwrite the value which may indicate they are a repeat donor.)
		if donor_id not in self.donors:
			# Record the year they donated so that we can detect later if they are a repeat donor.
			self.donors[donor_id] = year

	def is_repeat(self, donor_id, year):
		""" Tells you whether the donor is really a repeat donor. """
		if donor_id in self.donors:
			# A person becomes a repeat donor when they have donated in two *different* years.
			if year != self.donors[donor_id]:
				# Set year to 'None'.  This is how we mark them permanently as a repeat donor!
				self.donors[donor_id] = None
				return True
		return False


class Contributions:
	""" A place to record all repeat contributions, a.k.a. contribs.  'constribs' are constributions from *repeat donors* only.  Contribs EXCLUDE all donations before we found out the donor was a repeat donor. """
	def __init__(self):
		""" 'contibs' holds the amounts of donations from repeat donors, organized by year, zip-code, and recipient. """
		self.contribs = dict()

	def add(self, amount, block_id):
		""" Takes in an amount and adds the contribution to the appropriate list.  WARNING, this method does NOT check/enforce that the contribution is truly a repeat contribution. """
		if block_id not in self.contribs:
			self.contribs[block_id] = list()
		self.contribs[block_id].append(amount)

	def num(self, block_id):
		""" The number of contributions for that particular (year, zip-code, and recipient) (block_id). """
		return len(self.contribs[block_id])

	def amount(self, block_id):
		""" The total amount of contributions for that particular block_id. """
		return sum(self.contribs[block_id])

	def percentile_amount(self, percentile, block_id):
		""" The ordinal rank percentile amount for that particular block_id. """
		contrib_amounts = self.contribs[block_id]
		return ordinal_rank_percentile(percentile, contrib_amounts)

	def stats(self, percentile, year, zip_code, recipient, block_id):
		""" Return stats about the data """
		percentile_contrib = str(self.percentile_amount(percentile, block_id))
		total_contrib_amount = str(self.amount(block_id))
		num_contribs = str(self.num(block_id))

		output_list = [recipient, zip_code, year, percentile_contrib, total_contrib_amount, num_contribs]
		output_string = '|'.join(output_list) + '\n'
		return output_string

