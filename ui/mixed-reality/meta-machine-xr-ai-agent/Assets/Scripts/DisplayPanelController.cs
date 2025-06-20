using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[RequireComponent(typeof(OVRHand))]
public class DisplayPanelController : MonoBehaviour
{
    // Start is called before the first frame update
    private OVRHand ovrHand;
    public GameObject displayPanel;
    
    void Start()
    {
        ovrHand = GetComponent<OVRHand>();
        // Example: Set displayPanel's parent to ovrHand's transform
        //displayPanel.transform.position = ovrHand.transform.position;
        Camera mainCamera = Camera.main;
        if (mainCamera != null)
        {
            Vector3 cameraForward = mainCamera.transform.forward;
            Vector3 cameraPosition = mainCamera.transform.position;

            // Flatten the forward vector to keep the panel at eye level
            cameraForward.y = 0;
            cameraForward.Normalize();

            float distanceInFront = 1.5f; // Adjust as needed
            Vector3 panelPosition = cameraPosition + cameraForward * distanceInFront;

            // Set the panel's position and make it face the user
            displayPanel.transform.position = panelPosition;
            displayPanel.transform.LookAt(cameraPosition);
            displayPanel.transform.rotation = Quaternion.Euler(0, displayPanel.transform.rotation.eulerAngles.y, 0);
        }
    }
    private IEnumerator SetPanelAtHandPositionNextFrame()
    {
        yield return null; // Waits for the first frame to finish
        displayPanel.transform.position = ovrHand.transform.position;
    }

    // Update is called once per frame
    void Update()
    {

    }
}
