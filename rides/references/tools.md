# Meter Rides MCP tools

Generated from the `@meterapp/meter-sdk` catalog (server version 2.0.1); do not edit by hand. Server: `https://www.meterapp.co/api/mcp/rider`. The live server describes itself too: call `describe_api` for this list and `explain_data` for any result field.

| Tool | Personas | Writes? | Returns |
| --- | --- | --- | --- |
| [`submit_feedback`](tools/part-1.md#submit_feedback) | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | yes (saved proposal + confirmation) | FeedbackSubmissionWrite |
| [`vote_on_idea`](tools/part-1.md#vote_on_idea) | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | yes (saved proposal + confirmation) | FeedbackVoteWrite |
| [`follow_feedback_item`](tools/part-1.md#follow_feedback_item) | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | yes (saved proposal + confirmation) | FeedbackFollowWrite |
| [`comment_on_feedback_item`](tools/part-1.md#comment_on_feedback_item) | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | yes (saved proposal + confirmation) | FeedbackCommentWrite |
| [`list_feedback_categories`](tools/part-1.md#list_feedback_categories) | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | no | FeedbackCategories |
| [`list_ideas`](tools/part-1.md#list_ideas) | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | no | FeedbackItemPage |
| [`find_similar_ideas`](tools/part-1.md#find_similar_ideas) | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | no | FeedbackSimilarIdeas |
| [`list_my_feedback`](tools/part-1.md#list_my_feedback) | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | no | FeedbackItemPage |
| [`get_feedback_item`](tools/part-1.md#get_feedback_item) | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | no | FeedbackDetail |
| [`list_changelog`](tools/part-1.md#list_changelog) | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | no | FeedbackChangelogPage |
| [`find_tools`](tools/part-1.md#find_tools) | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | no | text |
| [`run_read_tool`](tools/part-1.md#run_read_tool) | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | no | text |
| [`run_write_tool`](tools/part-1.md#run_write_tool) | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | yes (saved proposal + confirmation) | text |
| [`list_change_requests`](tools/part-1.md#list_change_requests) | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | no | ChangeRequestPage |
| [`whoami`](tools/part-1.md#whoami) | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | no | Whoami |
| [`describe_api`](tools/part-1.md#describe_api) | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | no | text |
| [`explain_data`](tools/part-1.md#explain_data) | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | no | text |
| [`quote_booking`](tools/part-1.md#quote_booking) | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | no | BookingQuoteEstimate |
| [`list_bookings`](tools/part-1.md#list_bookings) | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | no | BookingPage |
| [`get_booking`](tools/part-1.md#get_booking) | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | no | Booking |
| [`get_booking_audit_log`](tools/part-1.md#get_booking_audit_log) | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | no | BookingAuditLog |
| [`cancel_booking`](tools/part-1.md#cancel_booking) | fleet_owner, fleet_admin, fleet_driver, solo_driver, rider | yes (saved proposal + confirmation) | BookingCancellationWrite |
| [`find_fleets`](tools/part-1.md#find_fleets) | rider | no | RiderFleetPage |
| [`search_places`](tools/part-1.md#search_places) | rider | no | PlaceSearch |
| [`estimate_ride`](tools/part-1.md#estimate_ride) | rider | no | RideEstimate |
| [`request_ride`](tools/part-1.md#request_ride) | rider | yes (saved proposal + confirmation) | RideRequestWrite |
| [`get_ride_status`](tools/part-1.md#get_ride_status) | rider | no | RideStatus |
| [`change_ride`](tools/part-1.md#change_ride) | rider | yes (saved proposal + confirmation) | RideChangeWrite |
| [`update_ride_details`](tools/part-1.md#update_ride_details) | rider | yes (saved proposal + confirmation) | RideDetailsWrite |
| [`respond_to_quote`](tools/part-1.md#respond_to_quote) | rider | yes (saved proposal + confirmation) | QuoteResponseWrite |
| [`get_rating_prompt`](tools/part-1.md#get_rating_prompt) | rider | no | RatingPrompt |
| [`rate_ride`](tools/part-1.md#rate_ride) | rider | yes (saved proposal + confirmation) | RideRatingWrite |
| [`report_ride_issue`](tools/part-1.md#report_ride_issue) | rider | yes (saved proposal + confirmation) | RideIssueReportWrite |
| [`list_quotes`](tools/part-1.md#list_quotes) | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | no | QuotePage |
| [`get_quote`](tools/part-1.md#get_quote) | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | no | QuoteDetail |
| [`get_action_link`](tools/part-1.md#get_action_link) | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | no | ActionLink |
| [`get_meter_pay_status`](tools/part-1.md#get_meter_pay_status) | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | no | MeterPayStatus |

Personas: `solo_driver` = driver using Meter independently; `fleet_driver` = driver belonging to a fleet; `fleet_admin` = administrator of a fleet; `fleet_owner` = owner of a fleet; `rider` = person booking rides.
