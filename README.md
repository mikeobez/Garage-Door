# Garage-Door
a repo for improvements to the garage door opener interface

Desired functionality:
- Any improvements must work with existing garage door interfaces
- Control and monitor garage door status from simple interfaces

Want to be able to interact with the system:
- Using the existing button by the door between house and garage (no work needed, just leave the button there)
- Using a keypad button (does not yet exist) on the door frame
- Using the garage door openers in the cars (only in two cars)
- Using an app
- Automatically (if desired)

Things to consider:
- I will not always have a phone on me
- Must be able to operate with multiple users
- It must be more than a simple trigger. There will be cases where the wifi will disconnect from the trigger device, and upon reconnecting it must not blindly open the garage door.
- There needs to be a way for the garage opener to identify the device that will trigger the door to open. This is ideally something that is not reproducable by other devices.

Security Considerations
- Only the permitted devices should be allowed to open the garage door. 
