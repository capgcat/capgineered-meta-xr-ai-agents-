using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DisplayPanelPositioning : MonoBehaviour
{
    // Start is called before the first frame update
    public GameObject root; // Reference to the root GameObject of your content
    private bool _hasPositioned = false; // Flag to check if already positioned
    void Start()
    {
        //InFrontOfUser();
    }

    // Update is called once per frame
    void Update()
    {
        if (!_hasPositioned)
        {
            InFrontOfUser();
            _hasPositioned = true;
        }
    }
    void InFrontOfUser()
    {
        // Reference to user's head (camera)
        Transform head = Camera.main.transform;

        // Reference to your content root (parent of all objects)
        Transform contentRoot = root.transform; // Replace with actual root GameObject

        // Desired distance in front of user
        float distanceInFront = 0.6f;

        // Calculate new position in front of the headset
        Vector3 newPosition = head.position + head.forward * distanceInFront;
        // Offset slightly to the left of the user's forward direction
        Vector3 leftOffset = -head.right * 0.6f; // 0.3 units to the left
        newPosition += leftOffset;
        // Move content root to that position
        contentRoot.position = newPosition;

        // Optionally face the user
        Vector3 lookDirection = head.forward;
        lookDirection.y = 0; // Keep it level
        contentRoot.rotation = Quaternion.LookRotation(lookDirection);
    }
}
