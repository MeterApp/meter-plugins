# Meter MCP tools

Generated from the `@meterapp/meter-sdk` catalog (server version 1.2.0); do not edit by hand. Servers: `https://www.meterapp.co/api/mcp/rider` (rider), `https://www.meterapp.co/api/mcp/fleet` (fleet), `https://www.meterapp.co/api/mcp` (both). The live server describes itself too: call `describe_api` for this list and `explain_data` for any result field.

| Tool | Servers | Personas | Writes? | Returns |
| --- | --- | --- | --- | --- |
| [`get_reconciliation_policies`](tools/part-1.md#get_reconciliation_policies) | fleet | fleet_owner, fleet_admin | no | ReconciliationPolicies |
| [`get_reconciliation_statements`](tools/part-1.md#get_reconciliation_statements) | fleet | fleet_owner, fleet_admin, fleet_driver | no | ReconciliationStatements |
| [`manage_reconciliation_policy`](tools/part-1.md#manage_reconciliation_policy) | fleet | fleet_owner, fleet_admin | yes (saved proposal + confirmation) | ReconciliationWrite |
| [`create_reconciliation_assessments`](tools/part-1.md#create_reconciliation_assessments) | fleet | fleet_owner, fleet_admin | yes (saved proposal + confirmation) | ReconciliationWrite |
| [`manage_reconciliation_assessment`](tools/part-1.md#manage_reconciliation_assessment) | fleet | fleet_owner, fleet_admin | yes (saved proposal + confirmation) | ReconciliationWrite |
| [`list_metrics`](tools/part-1.md#list_metrics) | fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner | no | MetricRegistry |
| [`query_metrics`](tools/part-1.md#query_metrics) | fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner | no | MetricQueryResult |
| [`list_reviews`](tools/part-1.md#list_reviews) | fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner | no | ReviewsPage |
| [`void_invoice`](tools/part-1.md#void_invoice) | fleet | solo_driver, fleet_owner, fleet_admin | yes (saved proposal + confirmation) | TripInvoiceVoidedWrite |
| [`create_invoice`](tools/part-1.md#create_invoice) | fleet | solo_driver, fleet_owner, fleet_admin | yes (saved proposal + confirmation) | TripInvoiceCreatedWrite |
| [`list_trip_invoices`](tools/part-1.md#list_trip_invoices) | fleet | solo_driver, fleet_owner, fleet_admin | no | TripInvoicePage |
| [`get_trip_invoice`](tools/part-1.md#get_trip_invoice) | fleet | solo_driver, fleet_owner, fleet_admin | no | TripInvoiceDetail |
| [`update_fee_settings`](tools/part-1.md#update_fee_settings) | fleet | fleet_owner, fleet_admin | yes (saved proposal + confirmation) | FleetFeeSettingsWrite |
| [`update_fleet_finances`](tools/part-1.md#update_fleet_finances) | fleet | fleet_owner, fleet_admin | yes (saved proposal + confirmation) | FleetFinanceSettingsWrite |
| [`submit_feedback`](tools/part-1.md#submit_feedback) | rider + fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | yes (saved proposal + confirmation) | FeedbackSubmissionWrite |
| [`vote_on_idea`](tools/part-1.md#vote_on_idea) | rider + fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | yes (saved proposal + confirmation) | FeedbackVoteWrite |
| [`follow_feedback_item`](tools/part-1.md#follow_feedback_item) | rider + fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | yes (saved proposal + confirmation) | FeedbackFollowWrite |
| [`comment_on_feedback_item`](tools/part-1.md#comment_on_feedback_item) | rider + fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | yes (saved proposal + confirmation) | FeedbackCommentWrite |
| [`list_feedback_categories`](tools/part-1.md#list_feedback_categories) | rider + fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | no | FeedbackCategories |
| [`list_ideas`](tools/part-1.md#list_ideas) | rider + fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | no | FeedbackItemPage |
| [`find_similar_ideas`](tools/part-1.md#find_similar_ideas) | rider + fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | no | FeedbackSimilarIdeas |
| [`list_my_feedback`](tools/part-1.md#list_my_feedback) | rider + fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | no | FeedbackItemPage |
| [`get_feedback_item`](tools/part-1.md#get_feedback_item) | rider + fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | no | FeedbackDetail |
| [`list_changelog`](tools/part-1.md#list_changelog) | rider + fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | no | FeedbackChangelogPage |
| [`find_tools`](tools/part-1.md#find_tools) | rider + fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | no | text |
| [`run_read_tool`](tools/part-1.md#run_read_tool) | rider + fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | no | text |
| [`run_write_tool`](tools/part-1.md#run_write_tool) | rider + fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | yes (saved proposal + confirmation) | text |
| [`list_change_requests`](tools/part-1.md#list_change_requests) | rider + fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | no | ChangeRequestPage |
| [`whoami`](tools/part-1.md#whoami) | rider + fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | no | Whoami |
| [`describe_api`](tools/part-1.md#describe_api) | rider + fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | no | text |
| [`explain_data`](tools/part-1.md#explain_data) | rider + fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | no | text |
| [`update_my_profile`](tools/part-1.md#update_my_profile) | fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner | yes (saved proposal + confirmation) | MyProfileWrite |
| [`update_my_availability`](tools/part-1.md#update_my_availability) | fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner | yes (saved proposal + confirmation) | DriverAvailabilityWrite |
| [`list_fleets`](tools/part-1.md#list_fleets) | fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner | no | FleetSummary |
| [`get_fleet`](tools/part-1.md#get_fleet) | fleet | fleet_driver, fleet_admin, fleet_owner | no | FleetDetail |
| [`update_fleet_settings`](tools/part-1.md#update_fleet_settings) | fleet | fleet_admin, fleet_owner | yes (saved proposal + confirmation) | FleetSettingsWrite |
| [`get_onboarding_checklist`](tools/part-1.md#get_onboarding_checklist) | fleet | fleet_admin, fleet_owner | no | OnboardingChecklist |
| [`list_fleet_members`](tools/part-1.md#list_fleet_members) | fleet | fleet_admin, fleet_owner | no | FleetMember |
| [`get_join_link`](tools/part-1.md#get_join_link) | fleet | fleet_admin, fleet_owner | no | FleetJoinLink |
| [`rotate_join_code`](tools/part-1.md#rotate_join_code) | fleet | fleet_admin, fleet_owner | yes (saved proposal + confirmation) | FleetJoinLinkWrite |
| [`remove_fleet_member`](tools/part-1.md#remove_fleet_member) | fleet | fleet_admin, fleet_owner | yes (saved proposal + confirmation) | FleetMemberRemovalWrite |
| [`update_member_name`](tools/part-1.md#update_member_name) | fleet | fleet_admin, fleet_owner | yes (saved proposal + confirmation) | FleetMemberNameWrite |
| [`get_membership_events`](tools/part-1.md#get_membership_events) | fleet | fleet_admin, fleet_owner | no | MembershipEventPage |
| [`set_member_online_state`](tools/part-1.md#set_member_online_state) | fleet | fleet_admin, fleet_owner | yes (saved proposal + confirmation) | MemberOnlineRequestWrite |
| [`list_member_documents`](tools/part-1.md#list_member_documents) | fleet | fleet_admin, fleet_owner | no | MemberDocumentsPage |
| [`review_member_document`](tools/part-1.md#review_member_document) | fleet | fleet_admin, fleet_owner | yes (saved proposal + confirmation) | MemberDocumentsWrite |
| [`list_vehicles`](tools/part-1.md#list_vehicles) | fleet | fleet_driver, fleet_admin, fleet_owner | no | Vehicle |
| [`assign_vehicle`](tools/part-1.md#assign_vehicle) | fleet | fleet_admin, fleet_owner | yes (saved proposal + confirmation) | VehicleAssignmentWrite |
| [`update_vehicle`](tools/part-1.md#update_vehicle) | fleet | fleet_admin, fleet_owner | yes (saved proposal + confirmation) | VehicleUpdateWrite |
| [`remove_vehicle`](tools/part-1.md#remove_vehicle) | fleet | fleet_admin, fleet_owner | yes (saved proposal + confirmation) | VehicleRemovalWrite |
| [`update_ride_option`](tools/part-1.md#update_ride_option) | fleet | fleet_admin, fleet_owner | yes (saved proposal + confirmation) | RideOptionWrite |
| [`create_ride_option`](tools/part-1.md#create_ride_option) | fleet | fleet_admin, fleet_owner | yes (saved proposal + confirmation) | RideOptionStateWrite |
| [`delete_ride_option`](tools/part-1.md#delete_ride_option) | fleet | fleet_admin, fleet_owner | yes (saved proposal + confirmation) | RideOptionStateWrite |
| [`list_zone_fares`](tools/part-1.md#list_zone_fares) | fleet | fleet_admin, fleet_owner | no | ZoneFarePage |
| [`set_zone_fare`](tools/part-1.md#set_zone_fare) | fleet | fleet_admin, fleet_owner | yes (saved proposal + confirmation) | ZoneFareWrite |
| [`find_zone_boundary`](tools/part-1.md#find_zone_boundary) | fleet | fleet_admin, fleet_owner | no | ZoneBoundary |
| [`save_service_zone`](tools/part-1.md#save_service_zone) | fleet | fleet_admin, fleet_owner | yes (saved proposal + confirmation) | ServiceZoneWrite |
| [`list_promo_codes`](tools/part-1.md#list_promo_codes) | fleet | fleet_admin, fleet_owner | no | PromoCodeList |
| [`create_promo_code`](tools/part-1.md#create_promo_code) | fleet | fleet_admin, fleet_owner | yes (saved proposal + confirmation) | PromoCodeWrite |
| [`update_promo_code`](tools/part-1.md#update_promo_code) | fleet | fleet_admin, fleet_owner | yes (saved proposal + confirmation) | PromoCodeWrite |
| [`disable_promo_code`](tools/part-1.md#disable_promo_code) | fleet | fleet_admin, fleet_owner | yes (saved proposal + confirmation) | PromoCodeWrite |
| [`email_promo_code`](tools/part-1.md#email_promo_code) | fleet | fleet_admin, fleet_owner | yes (saved proposal + confirmation) | PromoCodeEmailWrite |
| [`get_dynamic_pricing`](tools/part-1.md#get_dynamic_pricing) | fleet | fleet_admin, fleet_owner | no | DynamicPricing |
| [`update_dynamic_pricing`](tools/part-1.md#update_dynamic_pricing) | fleet | fleet_admin, fleet_owner | yes (saved proposal + confirmation) | DynamicPricingWrite |
| [`list_official_rates`](tools/part-1.md#list_official_rates) | fleet | fleet_admin, fleet_owner | no | OfficialRateList |
| [`import_official_rate`](tools/part-1.md#import_official_rate) | fleet | fleet_admin, fleet_owner | yes (saved proposal + confirmation) | OfficialRateImportWrite |
| [`list_known_locations`](tools/part-1.md#list_known_locations) | fleet | fleet_admin, fleet_owner | no | KnownLocationList |
| [`create_known_location`](tools/part-1.md#create_known_location) | fleet | fleet_admin, fleet_owner | yes (saved proposal + confirmation) | KnownLocationWrite |
| [`update_known_location`](tools/part-1.md#update_known_location) | fleet | fleet_admin, fleet_owner | yes (saved proposal + confirmation) | KnownLocationWrite |
| [`delete_known_location`](tools/part-1.md#delete_known_location) | fleet | fleet_admin, fleet_owner | yes (saved proposal + confirmation) | KnownLocationWrite |
| [`list_service_zones`](tools/part-1.md#list_service_zones) | fleet | fleet_admin, fleet_owner | no | ServiceZoneList |
| [`set_zone_fares`](tools/part-1.md#set_zone_fares) | fleet | fleet_admin, fleet_owner | yes (saved proposal + confirmation) | ZoneFaresWrite |
| [`generate_fleet_icons`](tools/part-1.md#generate_fleet_icons) | fleet | fleet_admin, fleet_owner | no | FleetIconCandidates |
| [`create_vehicle`](tools/part-1.md#create_vehicle) | fleet | fleet_admin, fleet_owner | yes (saved proposal + confirmation) | VehicleWrite |
| [`add_fleet_driver`](tools/part-1.md#add_fleet_driver) | fleet | fleet_admin, fleet_owner | yes (saved proposal + confirmation) | FleetMemberWrite |
| [`update_fleet_member`](tools/part-1.md#update_fleet_member) | fleet | fleet_admin, fleet_owner | yes (saved proposal + confirmation) | FleetMemberSettingsWrite |
| [`list_fares`](tools/part-1.md#list_fares) | fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner | no | FareReadPage |
| [`get_fare`](tools/part-1.md#get_fare) | fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner | no | FareRead |
| [`get_fare_audit_log`](tools/part-1.md#get_fare_audit_log) | fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner | no | FareAuditPage |
| [`create_fare`](tools/part-1.md#create_fare) | fleet | solo_driver, fleet_admin, fleet_owner | yes (saved proposal + confirmation) | FareWrite |
| [`update_fare`](tools/part-1.md#update_fare) | fleet | solo_driver, fleet_admin, fleet_owner | yes (saved proposal + confirmation) | FareWrite |
| [`delete_fare`](tools/part-1.md#delete_fare) | fleet | solo_driver, fleet_admin, fleet_owner | yes (saved proposal + confirmation) | FareWrite |
| [`get_booking_calendar`](tools/part-1.md#get_booking_calendar) | fleet | solo_driver, fleet_admin, fleet_owner | no | BookingCalendar |
| [`quote_booking`](tools/part-1.md#quote_booking) | rider + fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | no | BookingQuoteEstimate |
| [`list_bookings`](tools/part-1.md#list_bookings) | rider + fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | no | BookingPage |
| [`get_booking`](tools/part-1.md#get_booking) | rider + fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | no | Booking |
| [`get_booking_audit_log`](tools/part-1.md#get_booking_audit_log) | rider + fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | no | BookingAuditLog |
| [`update_booking_settings`](tools/part-1.md#update_booking_settings) | fleet | fleet_admin, fleet_owner | yes (saved proposal + confirmation) | BookingSettingsWrite |
| [`assign_booking`](tools/part-1.md#assign_booking) | fleet | fleet_owner, fleet_admin | yes (saved proposal + confirmation) | BookingChangeWrite |
| [`unassign_booking`](tools/part-2.md#unassign_booking) | fleet | fleet_owner, fleet_admin | yes (saved proposal + confirmation) | BookingChangeWrite |
| [`update_booking`](tools/part-2.md#update_booking) | fleet | fleet_owner, fleet_admin, fleet_driver, solo_driver | yes (saved proposal + confirmation) | BookingChangeWrite |
| [`cancel_booking`](tools/part-2.md#cancel_booking) | rider + fleet | fleet_owner, fleet_admin, fleet_driver, solo_driver, rider | yes (saved proposal + confirmation) | BookingCancellationWrite |
| [`send_payment_reminder`](tools/part-2.md#send_payment_reminder) | fleet | fleet_owner, fleet_admin | yes (saved proposal + confirmation) | BookingPaymentReminderWrite |
| [`accept_booking`](tools/part-2.md#accept_booking) | fleet | fleet_owner, fleet_admin, fleet_driver, solo_driver | yes (saved proposal + confirmation) | BookingLifecycleWrite |
| [`record_booking_progress`](tools/part-2.md#record_booking_progress) | fleet | fleet_owner, fleet_admin, fleet_driver, solo_driver | yes (saved proposal + confirmation) | BookingLifecycleWrite |
| [`complete_booking`](tools/part-2.md#complete_booking) | fleet | fleet_owner, fleet_admin, fleet_driver, solo_driver | yes (saved proposal + confirmation) | BookingLifecycleWrite |
| [`report_booking_no_show`](tools/part-2.md#report_booking_no_show) | fleet | fleet_owner, fleet_admin, fleet_driver, solo_driver | yes (saved proposal + confirmation) | BookingLifecycleWrite |
| [`change_booking_pickup_time`](tools/part-2.md#change_booking_pickup_time) | fleet | fleet_owner, fleet_admin, fleet_driver, solo_driver | yes (saved proposal + confirmation) | BookingLifecycleWrite |
| [`list_dispatch_offers`](tools/part-2.md#list_dispatch_offers) | fleet | fleet_owner, fleet_admin, fleet_driver | no | DispatchOffers |
| [`respond_to_dispatch_offer`](tools/part-2.md#respond_to_dispatch_offer) | fleet | fleet_owner, fleet_admin, fleet_driver | yes (saved proposal + confirmation) | DispatchOfferWrite |
| [`list_customers`](tools/part-2.md#list_customers) | fleet | fleet_owner, fleet_admin, solo_driver | no | CustomerPage |
| [`get_customer`](tools/part-2.md#get_customer) | fleet | fleet_owner, fleet_admin, solo_driver | no | CustomerDetail |
| [`create_booking`](tools/part-2.md#create_booking) | fleet | fleet_owner, fleet_admin | yes (saved proposal + confirmation) | OperatorBookingWrite |
| [`book_quote`](tools/part-2.md#book_quote) | fleet | fleet_owner, fleet_admin, solo_driver | yes (saved proposal + confirmation) | QuoteBookingConversionWrite |
| [`create_customer`](tools/part-2.md#create_customer) | fleet | fleet_owner, fleet_admin, solo_driver | yes (saved proposal + confirmation) | CustomerWrite |
| [`update_customer`](tools/part-2.md#update_customer) | fleet | fleet_owner, fleet_admin, solo_driver | yes (saved proposal + confirmation) | CustomerWrite |
| [`import_customers`](tools/part-2.md#import_customers) | fleet | fleet_owner, fleet_admin, solo_driver | yes (saved proposal + confirmation) | CustomerImportWrite |
| [`request_trip_void`](tools/part-2.md#request_trip_void) | fleet | fleet_owner, fleet_admin, fleet_driver | yes (saved proposal + confirmation) | TripVoidRequestWrite |
| [`review_trip_void`](tools/part-2.md#review_trip_void) | fleet | fleet_owner, fleet_admin | yes (saved proposal + confirmation) | TripVoidRequestWrite |
| [`update_trip_note`](tools/part-2.md#update_trip_note) | fleet | fleet_owner, fleet_admin, fleet_driver, solo_driver | yes (saved proposal + confirmation) | TripNoteWrite |
| [`find_fleets`](tools/part-2.md#find_fleets) | rider | rider | no | RiderFleetPage |
| [`search_places`](tools/part-2.md#search_places) | rider | rider | no | PlaceSearch |
| [`estimate_ride`](tools/part-2.md#estimate_ride) | rider | rider | no | RideEstimate |
| [`request_ride`](tools/part-2.md#request_ride) | rider | rider | yes (saved proposal + confirmation) | RideRequestWrite |
| [`get_ride_status`](tools/part-2.md#get_ride_status) | rider | rider | no | RideStatus |
| [`change_ride`](tools/part-2.md#change_ride) | rider | rider | yes (saved proposal + confirmation) | RideChangeWrite |
| [`update_ride_details`](tools/part-2.md#update_ride_details) | rider | rider | yes (saved proposal + confirmation) | RideDetailsWrite |
| [`respond_to_quote`](tools/part-2.md#respond_to_quote) | rider | rider | yes (saved proposal + confirmation) | QuoteResponseWrite |
| [`get_rating_prompt`](tools/part-2.md#get_rating_prompt) | rider | rider | no | RatingPrompt |
| [`rate_ride`](tools/part-2.md#rate_ride) | rider | rider | yes (saved proposal + confirmation) | RideRatingWrite |
| [`report_ride_issue`](tools/part-2.md#report_ride_issue) | rider | rider | yes (saved proposal + confirmation) | RideIssueReportWrite |
| [`send_quote`](tools/part-2.md#send_quote) | fleet | solo_driver, fleet_admin, fleet_owner | yes (saved proposal + confirmation) | QuoteActionWrite |
| [`extend_quote`](tools/part-2.md#extend_quote) | fleet | solo_driver, fleet_admin, fleet_owner | yes (saved proposal + confirmation) | QuoteActionWrite |
| [`withdraw_quote`](tools/part-2.md#withdraw_quote) | fleet | solo_driver, fleet_admin, fleet_owner | yes (saved proposal + confirmation) | QuoteActionWrite |
| [`follow_up_quote`](tools/part-2.md#follow_up_quote) | fleet | solo_driver, fleet_admin, fleet_owner | yes (saved proposal + confirmation) | QuoteActionWrite |
| [`create_quote`](tools/part-2.md#create_quote) | fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner | yes (saved proposal + confirmation) | QuoteWrite |
| [`price_quote`](tools/part-2.md#price_quote) | fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner | yes (saved proposal + confirmation) | QuoteWrite |
| [`list_quotes`](tools/part-2.md#list_quotes) | rider + fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | no | QuotePage |
| [`get_quote`](tools/part-2.md#get_quote) | rider + fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | no | QuoteDetail |
| [`add_trip_fee`](tools/part-2.md#add_trip_fee) | fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner | yes (saved proposal + confirmation) | TripAdjustmentWrite |
| [`remove_trip_fee`](tools/part-2.md#remove_trip_fee) | fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner | yes (saved proposal + confirmation) | TripAdjustmentWrite |
| [`add_trip_discount`](tools/part-2.md#add_trip_discount) | fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner | yes (saved proposal + confirmation) | TripAdjustmentWrite |
| [`remove_trip_discount`](tools/part-2.md#remove_trip_discount) | fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner | yes (saved proposal + confirmation) | TripAdjustmentWrite |
| [`mark_trip_cash_paid`](tools/part-2.md#mark_trip_cash_paid) | fleet | fleet_admin, fleet_owner | yes (saved proposal + confirmation) | TripAdjustmentWrite |
| [`list_trips`](tools/part-2.md#list_trips) | fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner | no | TripPage |
| [`search_trips`](tools/part-2.md#search_trips) | fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner | no | TripPage |
| [`get_trip`](tools/part-2.md#get_trip) | fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner | no | Trip |
| [`list_ledger_entries`](tools/part-2.md#list_ledger_entries) | fleet | fleet_admin, fleet_owner | no | LedgerEntryPage |
| [`list_driver_balances`](tools/part-2.md#list_driver_balances) | fleet | fleet_admin, fleet_owner | no | DriverBalancePage |
| [`get_driver_accounting`](tools/part-2.md#get_driver_accounting) | fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner | no | DriverAccounting |
| [`list_settlements`](tools/part-2.md#list_settlements) | fleet | fleet_admin, fleet_owner | no | SettlementPage |
| [`list_accounting_exceptions`](tools/part-2.md#list_accounting_exceptions) | fleet | fleet_admin, fleet_owner | no | AccountingExceptionPage |
| [`export_data`](tools/part-2.md#export_data) | fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner | no | DataExport |
| [`get_tax_summary`](tools/part-2.md#get_tax_summary) | fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner | no | TaxSummary |
| [`get_mileage_report`](tools/part-2.md#get_mileage_report) | fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner | no | MileageReport |
| [`get_earnings`](tools/part-2.md#get_earnings) | fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner | no | EarningsSummary |
| [`get_accounting_summary`](tools/part-2.md#get_accounting_summary) | fleet | fleet_admin, fleet_owner | no | AccountingSummary |
| [`get_action_link`](tools/part-2.md#get_action_link) | rider + fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | no | ActionLink |
| [`get_meter_pay_status`](tools/part-2.md#get_meter_pay_status) | rider + fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner, rider | no | MeterPayStatus |
| [`get_subscription`](tools/part-2.md#get_subscription) | fleet | solo_driver, fleet_admin, fleet_owner | no | SubscriptionOverview |
| [`list_plans`](tools/part-2.md#list_plans) | fleet | solo_driver, fleet_driver, fleet_admin, fleet_owner | no | PlanCatalog |
| [`get_website_page`](tools/part-2.md#get_website_page) | fleet | fleet_admin, fleet_owner | no | WebsitePage |
| [`list_website_pages`](tools/part-2.md#list_website_pages) | fleet | fleet_admin, fleet_owner | no | WebsitePages |
| [`create_website_page`](tools/part-2.md#create_website_page) | fleet | fleet_admin, fleet_owner | yes (saved proposal + confirmation) | WebsitePageWrite |
| [`update_website_page`](tools/part-2.md#update_website_page) | fleet | fleet_admin, fleet_owner | yes (saved proposal + confirmation) | WebsitePageWrite |
| [`delete_website_page`](tools/part-2.md#delete_website_page) | fleet | fleet_admin, fleet_owner | yes (saved proposal + confirmation) | WebsitePageWrite |
| [`get_storefront_settings`](tools/part-2.md#get_storefront_settings) | fleet | fleet_admin, fleet_owner | no | StorefrontSettings |
| [`update_storefront_settings`](tools/part-2.md#update_storefront_settings) | fleet | fleet_admin, fleet_owner | yes (saved proposal + confirmation) | StorefrontSettingsWrite |
| [`search_google_places`](tools/part-2.md#search_google_places) | fleet | fleet_admin, fleet_owner | no | GooglePlaceSearch |
| [`link_google_maps_place`](tools/part-2.md#link_google_maps_place) | fleet | fleet_admin, fleet_owner | yes (saved proposal + confirmation) | GoogleMapsLinkWrite |
| [`unlink_google_maps_place`](tools/part-2.md#unlink_google_maps_place) | fleet | fleet_admin, fleet_owner | yes (saved proposal + confirmation) | GoogleMapsLinkWrite |
| [`get_seo_overview`](tools/part-2.md#get_seo_overview) | fleet | fleet_admin, fleet_owner | no | SeoOverview |
| [`get_marketing_overview`](tools/part-2.md#get_marketing_overview) | fleet | fleet_admin, fleet_owner | no | MarketingOverview |
| [`get_driver_performance`](tools/part-2.md#get_driver_performance) | fleet | fleet_admin, fleet_owner | no | DriverPerformance |
| [`get_privacy_settings`](tools/part-2.md#get_privacy_settings) | fleet | fleet_admin, fleet_owner | no | PrivacySettings |
| [`update_privacy_settings`](tools/part-2.md#update_privacy_settings) | fleet | fleet_admin, fleet_owner | yes (saved proposal + confirmation) | PrivacySettingsWrite |
| [`get_voice_agent_settings`](tools/part-2.md#get_voice_agent_settings) | fleet | fleet_admin, fleet_owner | no | VoiceAgentSettings |
| [`update_voice_agent_settings`](tools/part-2.md#update_voice_agent_settings) | fleet | fleet_admin, fleet_owner | yes (saved proposal + confirmation) | VoiceAgentSettingsWrite |
| [`list_notification_webhooks`](tools/part-2.md#list_notification_webhooks) | fleet | fleet_admin, fleet_owner | no | NotificationWebhooks |

Personas: `solo_driver` = driver using Meter independently; `fleet_driver` = driver belonging to a fleet; `fleet_admin` = administrator of a fleet; `fleet_owner` = owner of a fleet; `rider` = person booking rides.
