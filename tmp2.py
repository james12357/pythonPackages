import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.tiia.v20190529 import tiia_client, models
try:
    cred = credential.Credential("AKIDf9KI0RaS3OSFm20h7G8j37tOcZFemcBT", "3pKZXEenfGadOt62h5B0YptgCRP6WfX8")
    httpProfile = HttpProfile()
    httpProfile.endpoint = "tiia.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = tiia_client.TiiaClient(cred, "ap-shanghai", clientProfile)

    req = models.AssessQualityRequest()
    params = {
        "ImageUrl": "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg.puchedu.cn%2Fuploads%2F0%2F15%2F3632931380%2F3781955071.jpg&refer=http%3A%2F%2Fimg.puchedu.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1641871071&t=a5a1b6fc6945688a7a3dbe5a27995157"
    }
    req.from_json_string(json.dumps(params))

    resp = client.AssessQuality(req)
    print(resp.to_json_string())

except TencentCloudSDKException as err:
    print(err)
