"use client";

import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { MoreHorizontal, Ban, Trash2 } from "lucide-react";
import { formatDistanceToNow } from "date-fns";

interface ApiKey {
  id: string;
  name: string | null;
  start: string | null;
  prefix: string | null;
  userId: string;
  enabled: boolean;
  expiresAt: Date | null;
  createdAt: Date;
  lastRequest: Date | null;
  metadata: Record<string, unknown> | null;
}

interface ApiKeyListProps {
  apiKeys: ApiKey[];
  isLoading: boolean;
  onRevoke: (key: ApiKey) => void;
  onDelete: (key: ApiKey) => void;
}

function getKeyStatus(key: ApiKey): { label: string; variant: "default" | "secondary" | "destructive" | "outline" } {
  if (!key.enabled) {
    return { label: "Revoked", variant: "destructive" };
  }
  if (key.expiresAt && new Date(key.expiresAt) < new Date()) {
    return { label: "Expired", variant: "secondary" };
  }
  return { label: "Active", variant: "default" };
}

function formatDate(date: Date | null): string {
  if (!date) return "Never";
  try {
    return formatDistanceToNow(new Date(date), { addSuffix: true });
  } catch {
    return "Invalid date";
  }
}

export function ApiKeyList({ apiKeys, isLoading, onRevoke, onDelete }: ApiKeyListProps) {
  if (isLoading) {
    return (
      <div className="flex items-center justify-center py-12">
        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-pana-500"></div>
      </div>
    );
  }

  if (apiKeys.length === 0) {
    return (
      <div className="text-center py-12">
        <p className="text-gray-500 mb-2">No API keys found</p>
        <p className="text-sm text-gray-400">
          Create your first API key to enable machine-to-machine authentication.
        </p>
      </div>
    );
  }

  return (
    <div className="rounded-md border">
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>Name</TableHead>
            <TableHead>Key Prefix</TableHead>
            <TableHead>Status</TableHead>
            <TableHead>Created</TableHead>
            <TableHead>Last Used</TableHead>
            <TableHead>Expires</TableHead>
            <TableHead className="w-[50px]"></TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {apiKeys.map((key) => {
            const status = getKeyStatus(key);
            return (
              <TableRow key={key.id}>
                <TableCell className="font-medium">
                  {key.name || "Unnamed Key"}
                </TableCell>
                <TableCell>
                  <code className="text-sm bg-gray-100 px-2 py-1 rounded">
                    {key.start || key.prefix || "—"}
                  </code>
                </TableCell>
                <TableCell>
                  <Badge variant={status.variant}>{status.label}</Badge>
                </TableCell>
                <TableCell className="text-sm text-gray-600">
                  {formatDate(key.createdAt)}
                </TableCell>
                <TableCell className="text-sm text-gray-600">
                  {formatDate(key.lastRequest)}
                </TableCell>
                <TableCell className="text-sm text-gray-600">
                  {key.expiresAt ? formatDate(key.expiresAt) : "Never"}
                </TableCell>
                <TableCell>
                  <DropdownMenu>
                    <DropdownMenuTrigger asChild>
                      <Button variant="ghost" size="sm" className="h-8 w-8 p-0">
                        <MoreHorizontal className="h-4 w-4" />
                      </Button>
                    </DropdownMenuTrigger>
                    <DropdownMenuContent align="end">
                      {key.enabled && (
                        <DropdownMenuItem
                          onClick={() => onRevoke(key)}
                          className="text-orange-600"
                        >
                          <Ban className="h-4 w-4 mr-2" />
                          Revoke
                        </DropdownMenuItem>
                      )}
                      <DropdownMenuItem
                        onClick={() => onDelete(key)}
                        className="text-red-600"
                      >
                        <Trash2 className="h-4 w-4 mr-2" />
                        Delete
                      </DropdownMenuItem>
                    </DropdownMenuContent>
                  </DropdownMenu>
                </TableCell>
              </TableRow>
            );
          })}
        </TableBody>
      </Table>
    </div>
  );
}
