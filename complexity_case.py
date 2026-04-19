def evaluate_order(order, flags):
    if order.get("is_new"):
        print("new")
    if order.get("is_priority"):
        print("priority")
    if order.get("has_discount"):
        print("discount")
    if order.get("needs_review"):
        print("review")
    if order.get("has_gift_wrap"):
        print("gift")
    if order.get("is_international"):
        print("international")
    if flags.get("notify_sales"):
        print("sales")
    if flags.get("notify_support"):
        print("support")
    if flags.get("notify_shipping"):
        print("shipping")
    if flags.get("notify_finance"):
        print("finance")
    if flags.get("notify_admin"):
        print("admin")
    if flags.get("notify_manager"):
        print("manager")
    if flags.get("requires_signature"):
        print("signature")
    if flags.get("expedite_carrier"):
        print("carrier")
    if flags.get("fraud_check"):
        print("fraud")
    if flags.get("manual_audit"):
        print("audit")
