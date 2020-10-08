using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class car_script : MonoBehaviour
{

    public string name;
    public bool isActive;
    public GameObject frontRight;
    public GameObject frontLeft;
    public GameObject rearRight;
    public GameObject rearLeft;

    // Start is called before the first frame update
    void Start()
    {
        Debug.Log("I am chris and this is my " + name);
        // isActive = false;
    }

    // Update is called once per frame
    void Update()
    {
        if (!this.isActive)
        {
            return;
        }


        HingeJoint rearLeftHingeJoint = rearLeft.GetComponent<HingeJoint>();
        HingeJoint rearRightHingeJoint = rearRight.GetComponent<HingeJoint>();
        HingeJoint frontLeftHingeJoint = frontLeft.GetComponent<HingeJoint>();
        HingeJoint frontRightHingeJoint = frontRight.GetComponent<HingeJoint>();

        var driveMotor = new JointMotor();
        var turnMotor = new JointMotor();

        driveMotor.force = 0;
        driveMotor.targetVelocity = 0;
        driveMotor.freeSpin = false;

        // set all to zero
        frontLeftHingeJoint.motor = frontRightHingeJoint.motor = rearLeftHingeJoint.motor = rearRightHingeJoint.motor = driveMotor;

        frontLeftHingeJoint.useMotor = frontRightHingeJoint.useMotor = rearLeftHingeJoint.useMotor = rearRightHingeJoint.useMotor = true;

        turnMotor.freeSpin = true;

        if (Input.GetKey("w"))
        {
            driveMotor.force = 1000;
            driveMotor.targetVelocity = 700;

            rearRightHingeJoint.motor = driveMotor;
            rearRightHingeJoint.useMotor = true;

            rearLeftHingeJoint.motor = driveMotor;
            rearLeftHingeJoint.useMotor = true;        


        }
        if (Input.GetKey("s"))
        {
            driveMotor.force = 1000;
            driveMotor.targetVelocity = -700;

            rearRightHingeJoint.motor = driveMotor;
            rearRightHingeJoint.useMotor = true;

            rearLeftHingeJoint.motor = driveMotor;
            rearLeftHingeJoint.useMotor = true;

        }
        if (Input.GetKey("a"))
        {
            turnMotor.force = 1000;
            turnMotor.targetVelocity = 700;

            frontRightHingeJoint.motor = rearRightHingeJoint.motor = turnMotor;
            frontRightHingeJoint.useMotor = rearRightHingeJoint.useMotor = true;
        }
        if (Input.GetKey("d"))
        {
            turnMotor.force = 1000;
            turnMotor.targetVelocity = 700;

            frontLeftHingeJoint.motor = rearLeftHingeJoint.motor = turnMotor;
            frontLeftHingeJoint.useMotor = rearLeftHingeJoint.useMotor = true;
        }       

    }
}
