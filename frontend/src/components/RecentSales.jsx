import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/Avatar";

export function RecentSales({ customers }) {
  const sortedCustomers = customers.sort((a, b) => b.id - a.id);

  const latestFiveCustomers = sortedCustomers.slice(0, 5);

  const generateRandomAmount = () => {
    return (Math.random() * 10000).toFixed(2);
  };

  return (
    <div className="space-y-8">
      {latestFiveCustomers.map((customer) => (
        <div key={customer.id} className="flex items-center">
          <Avatar className="h-9 w-9">
            <AvatarImage src={customer.avatar} alt="Avatar" />
            <AvatarFallback>{customer.initials}</AvatarFallback>
          </Avatar>
          <div className="ml-4 space-y-1">
            <p className="text-sm font-medium leading-none">{customer.name}</p>
            <p className="text-sm text-muted-foreground">{customer.email}</p>
          </div>
          <div className="ml-auto font-medium">
            +${generateRandomAmount()}
          </div>
        </div>
      ))}
    </div>
  );
}
