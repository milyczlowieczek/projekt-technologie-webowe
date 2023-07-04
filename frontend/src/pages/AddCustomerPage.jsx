import { MainNav } from "@/components/MainNav";
import { navigationLinks } from "../config/navigationLinks";
import { UserNav } from "./CustomersPage/components/UserNav";
import { useState } from "react";

export const AddCustomerPage = () => {
  const [name, submitName] = useState("");
  const [surname, submitSurname] = useState("")
  const [email, submitEmail] = useState("")
  const [phoneNumber, submitPhoneNumber] = useState("")
  const [successMessage, printSuccessMessage] = useState("");

  const submitForm = async (form) => {
    form.preventDefault();
    console.log(name, surname, email, phoneNumber);

    try {
      const response = await fetch("http://127.0.0.1:8000/customers", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          name: name,
          surname: surname,
          email: email,
          phoneNumber: phoneNumber,
        }),
      });
  
      if (response.ok) {
        const customer = await response.json();
        console.log(customer);
        printSuccessMessage("Customer created successfully!");
      } else {
        const errorResponse = await response.json();
        console.log("Error:", errorResponse);
        printSuccessMessage("");
      }
    } catch (error) {
      console.log("ERROR")
      printSuccessMessage("");
    }


    submitName("");
    submitSurname("");
    submitEmail("");
    submitPhoneNumber("");
  };

  return (
    <div className="hidden flex-col md:flex">
      <div className="border-b">
        <div className="flex h-16 items-center px-4">
          <MainNav className="mx-6" links={navigationLinks} />
          <div className="ml-auto flex items-center space-x-4">
            <UserNav />
          </div>
        </div>
      </div>
      <div className="flex-1 space-y-4 p-8 pt-6">
        <div className="flex items-center justify-between space-y-2">
          <h2 className="text-3xl font-bold tracking-tight">Add customer</h2>
        </div>
      <div className="hidden h-full flex-1 flex-col space-y-8 md:flex"></div>
        <form className="submitForm" onSubmit={ submitForm }>
          <input value={ name } onChange = { (form) => submitName(form.target.value) } placeholder="Name" type = "text"/>
          <input value={ surname } onChange = { (form) => submitSurname(form.target.value) } placeholder="Surname" type = "text"/>
          <input value={ email } onChange = { (form) => submitEmail(form.target.value) } placeholder="youremail@email.com" type = "email"/>
          <input value={ phoneNumber } onChange = { (form) => submitPhoneNumber(form.target.value) } placeholder="000-000-000" type = "text"/>
          {successMessage && (<p className="text-green-500">{successMessage}</p>)}
          <button type="submit">Add</button>
        </form>
      </div>
    </div>
  );
};
