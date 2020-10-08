using System.Collections;
using System.Collections.Generic;
using UnityEditor;
using UnityEngine;

public class setActive : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    List<GameObject> FindAllPrefabInstances(UnityEngine.Object CarFinal)
    {
        List<GameObject> result = new List<GameObject>();
        GameObject[] allObjects = (GameObject[])FindObjectsOfType(typeof(GameObject));
        foreach (GameObject GO in allObjects)
        {
            if (PrefabUtility.GetPrefabType(GO) == PrefabType.PrefabInstance)
            {
                UnityEngine.Object GO_prefab = PrefabUtility.GetPrefabParent(GO);
                if (CarFinal == GO_prefab)
                    result.Add(GO);
            }
        }
        return result;
    }

    // Update is called once per frame
    void Update()
    {
        for (int i = 0; i < 10; i++)
        {
            if (Input.GetKeyDown("" + i.ToString()))
            {
                //List<GameObject> cars = FindAllPrefabInstances(CarFinal);

                GameObject[] cars = GameObject.FindGameObjectsWithTag("Player");
                foreach (GameObject car in cars)
                {
                    car_script script = car.GetComponent<car_script>();

                    if (script.name == i.ToString())
                    {
                        script.isActive = true;
                    }
                    else
                    {
                        script.isActive = false;
                    }
                }
            }
        }
    }
}
