getObject = {
        'accountId': 1234,
        'address': '01-307608-ams01.clb.appdomain.cloud',
        'createDate': '2019-08-12T07:49:43-06:00',
        'id': 1111111,
        'isPublic': 0,
        'locationId': 265592,
        'modifyDate': '2019-08-13T16:26:06-06:00',
        'name': 'dcabero-01',
        'operatingStatus': 'ONLINE',
        'provisioningStatus': 'ACTIVE',
        'type': 0,
        'useSystemPublicIpPool': 1,
        'uuid': '1a1aa111-4474-4e16-9f02-4de959229b85',
        'listenerCount': 4,
        'memberCount': 1,
        'datacenter': {
            'id': 265592,
            'longName': 'Amsterdam 1',
            'name': 'ams01',
            'statusId': 2
        }
    }
getAllObjects = [getObject]


getLoadBalancerMemberHealth = [
    {
        'poolUuid': '1c5f3ba6-ec7d-4cf8-8815-9bb174224a76',
        'membersHealth': [
            {
                'status': 'DOWN',
                'uuid': 'ba23a166-faa4-4eb2-96e7-ef049d65ce60'
            }
        ]
    }
]

getLoadBalancer = {
    "accountId": 3071234,
    "createDate": "2019-08-12T21:49:43+08:00",
    "id": 81234,
    "isPublic": 0,
    "locationId": 265592,
    "modifyDate": "2019-08-14T06:26:06+08:00",
    "name": "dcabero-01",
    "uuid": "0a2da082-4474-4e16-9f02-4de11111",
    "datacenter": {
        "id": 265592,
        "longName": "Amsterdam 1",
        "name": "ams01",
        "statusId": 2
    }
}

getHealthMonitors = {}

getLoadBalancer = getObject
cancelLoadBalancer = getObject
