from userconnectio.models import ConnectionRequest
from users.models import CustomUser
from itertools import chain


def rb_recommend(user,request):

    sent_to = set() #to store all users that the 'user'(say A) sent requests to say(B)
    recommended_users = set() 
    all_connections_of_c = set()
    all_requests_sentby_c = set()
    # getting all the requests the 'user' sent to
    all_requests = ConnectionRequest.objects.filter(sender=user)

    # getting all the users to whom the request is sent ny the authenticated user
    for my_request in all_requests:
        get_user = CustomUser.objects.get(id=my_request.receiver.id)
        sent_to.add(get_user)
    sent_to=list(sent_to)
    print("All requests sent my the authenticated user:")
    print(sent_to)
    reqsender_to_b = []

    #now accessing the users(say C) that sent request to my users sent_to (B)
    for userB in sent_to:
        requests_receivedby_b = ConnectionRequest.objects.filter(receiver=userB).exclude(sender=request.user)
        reqsender_to_b = [user.sender for user in requests_receivedby_b]
    print("other users that sent requests to B:")
    print(reqsender_to_b)    

    # now access requests sent by reqsender_to_b (C)  to other users (D) along with connections of C (D)
    for sender in reqsender_to_b:
        print(f"for user {sender}:")
        requests_sent_by_c = ConnectionRequest.objects.filter(sender=sender).exclude(receiver=request.user)


        connections_of_c = sender.connections.all()


        print(f"requests sent by {sender}:: {requests_sent_by_c}")
        print(f"connections of {sender}:: {connections_of_c}")
        all_connections_of_c.update(connections_of_c)
        all_requests_sentby_c.update(requests_sent_by_c)
    print("final result:")
    print("All requests sent by C")    
    print(all_requests_sentby_c)
    print("All connections of C")
    print(all_connections_of_c)

    #getting actual user of the connectionlist and requestlist (stored in D)
    print("fun begins here")

    #removing users that are already a connection 
    existing_connections = request.user.connections.all()
    existing_request_sent = ConnectionRequest.objects.filter(sender=request.user,is_active=True)

    all_connections_of_c = [user for user in all_connections_of_c if user not in existing_connections]
    recommended_users=set([singleuser.user for singleuser in all_connections_of_c])
        
    for singleuser in all_requests_sentby_c:
        userd = singleuser.receiver
        recommended_users.add(userd)
    existing_connected_users=[user.user for user in existing_connections]
    existing_request_sent_users = [user.receiver for user in existing_request_sent]
    
    recommended_users = [user for user in recommended_users if user not in existing_connected_users]
    if request.user in recommended_users:
        recommended_users.remove(request.user)
    recommended_users = list(set(recommended_users)-set(existing_request_sent_users)-set(existing_connected_users))

    print("existing connections")
    print(existing_connected_users)
    print("existing requests")
    print(existing_request_sent_users)
    
    print("recomm")
    print(recommended_users)
    return recommended_users
   



   