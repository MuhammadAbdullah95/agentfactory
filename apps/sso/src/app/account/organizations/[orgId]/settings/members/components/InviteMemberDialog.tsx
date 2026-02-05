"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog";
import { Input } from "@/components/ui/input";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { toast } from "@/lib/utils/toast";
import { authClient } from "@/lib/auth-client";
import { useRouter } from "next/navigation";

// Better Auth default roles for invitations
// Custom roles (manager, proctor, editor) can be assigned after member joins
type InviteRole = "member" | "admin" | "owner";

const INVITE_ROLES: { value: InviteRole; label: string; description: string }[] = [
  { value: "member", label: "Member", description: "Read-only access" },
  { value: "admin", label: "Admin", description: "Full admin access" },
  { value: "owner", label: "Owner", description: "Full control" },
];

interface InviteMemberDialogProps {
  organizationId: string;
  organizationName: string;
}

export function InviteMemberDialog({ organizationId, organizationName }: InviteMemberDialogProps) {
  const router = useRouter();
  const [open, setOpen] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [formData, setFormData] = useState({
    email: "",
    role: "member" as InviteRole,
  });

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    // Validate email
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(formData.email)) {
      toast.error("Please enter a valid email address");
      return;
    }

    setIsLoading(true);

    try {
      await authClient.organization.inviteMember({
        organizationId,
        email: formData.email,
        role: formData.role,
      });

      toast.success(`Invitation sent to ${formData.email}`);
      setFormData({ email: "", role: "member" });
      setOpen(false);
      router.refresh();
    } catch (error: any) {
      console.error("Failed to send invitation:", error);

      if (error.message?.includes("rate limit")) {
        toast.error("Rate limit exceeded. Maximum 5 invitations per hour.");
      } else if (error.message?.includes("already a member")) {
        toast.error("This user is already a member of the organization");
      } else {
        toast.error("Failed to send invitation");
      }
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <Dialog open={open} onOpenChange={setOpen}>
      <DialogTrigger asChild>
        <Button>
          <svg className="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 4v16m8-8H4" />
          </svg>
          Invite Member
        </Button>
      </DialogTrigger>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>Invite Member</DialogTitle>
          <DialogDescription>
            Send an invitation to join {organizationName}
          </DialogDescription>
        </DialogHeader>

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label htmlFor="email" className="block text-sm font-medium text-slate-700 mb-2">
              Email Address
            </label>
            <Input
              id="email"
              type="email"
              value={formData.email}
              onChange={(e) => setFormData({ ...formData, email: e.target.value })}
              placeholder="colleague@example.com"
              required
            />
          </div>

          <div>
            <label htmlFor="role" className="block text-sm font-medium text-slate-700 mb-2">
              Role
            </label>
            <Select
              value={formData.role}
              onValueChange={(value) =>
                setFormData({ ...formData, role: value as InviteRole })
              }
            >
              <SelectTrigger>
                <SelectValue />
              </SelectTrigger>
              <SelectContent>
                {INVITE_ROLES.map((role) => (
                  <SelectItem key={role.value} value={role.value}>
                    {role.label} - {role.description}
                  </SelectItem>
                ))}
              </SelectContent>
            </Select>
          </div>

          <DialogFooter>
            <Button type="button" variant="outline" onClick={() => setOpen(false)} disabled={isLoading}>
              Cancel
            </Button>
            <Button type="submit" disabled={isLoading}>
              {isLoading ? "Sending..." : "Send Invitation"}
            </Button>
          </DialogFooter>
        </form>
      </DialogContent>
    </Dialog>
  );
}
