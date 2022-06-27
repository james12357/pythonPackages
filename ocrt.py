import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.ocr.v20181119 import ocr_client, models
try:
    cred = credential.Credential("AKIDf9KI0RaS3OSFm20h7G8j37tOcZFemcBT", "3pKZXEenfGadOt62h5B0YptgCRP6WfX8")
    httpProfile = HttpProfile()
    httpProfile.endpoint = "ocr.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = ocr_client.OcrClient(cred, "ap-shanghai", clientProfile)

    req = models.GeneralAccurateOCRRequest()
    params = {
        # "ImageBase64": "a",
        "ImageUrl": "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fnimg.ws.126.net%2F%3Furl%3Dhttp%3A%2F%2Fdingyue.ws.126.net%2F2021%2F0630%2F221132bfj00qvhu5a0027c000u000vcm.jpg%26thumbnail%3D650x2147483647%26quality%3D80%26type%3Djpg&refer=http%3A%2F%2Fnimg.ws.126.net&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1641871750&t=bdd58f4d6a1198d3e9e3373753e3c3f9"
    }
    req.from_json_string(json.dumps(params))

    resp = client.GeneralAccurateOCR(req)
    print(resp.to_json_string())

except TencentCloudSDKException as err:
    print(err)