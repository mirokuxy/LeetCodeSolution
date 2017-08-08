# 253. Meeting Rooms II
# https://leetcode.com/problems/meeting-rooms-ii/description/

# Solution: 
#   1) Every interval can be treated as two events: meeting start, meeting end
#   2) convert intervals to a list of sorted events, scan the list,
#       and we just need to calculate on the fly how many meetings are happening at the time,
#       and the maximum number of meetings during the time is the number of rooms we need.


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
  def minMeetingRooms(self, intervals):
    """
    :type intervals: List[Interval]
    :rtype: int
    """
    events = []
    for interval in intervals:
      events.append( (interval.start, 1) )
      events.append( (interval.end, -1) )
    events.sort()

    max_meetings = 0
    meetings = 0
    for event in events:
      _, diff = event
      meetings += diff
      max_meetings = max(max_meetings, meetings)

    return max_meetings


        