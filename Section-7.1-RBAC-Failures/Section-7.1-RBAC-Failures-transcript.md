# Section 7.1 — RBAC Failures (video transcript)

Use this as a spoken script for the `Section-7.1-RBAC-Failures` lab. Adjust pacing to your demo length.

---

Hi! In this section, we’re troubleshooting **RBAC** — **Role-Based Access Control**. RBAC is the core security mechanism in Kubernetes, but it can be frustrating when you or your apps hit that dreaded **`Forbidden`** error. 

Usually, the cause is a **missing binding**, a misspelled **verb**, or—most commonly—a **scoping issue** where you've used a **Role** to grant permissions in one namespace, but the app is trying to access resources in another. We’ll walk through how to use **impersonation** to test permissions and how to correctly scope your access.

---

First, let's create a ServiceAccount named **`dev-user`**. To test its permissions without actually logging in as that user, we use the **`--as`** flag. Note the format: **`system:serviceaccount:namespace:name`**. This is how Kubernetes internally identifies service account tokens.

Initially, a new ServiceAccount has zero permissions. If we try to **`get pods`**, we’ll get a **Forbidden** error. The most powerful tool in your belt here is **`kubectl auth can-i`**. It allows you to query the API server: *"Can this user perform this action?"* It’s much faster than trial-and-error.

---

To fix this, we apply **`role-and-binding.yaml`**. This creates a **Role** (which contains the rules) and a **RoleBinding** (which connects those rules to our user). 

Now, **`get pods`** works! But wait—if we try to **create** a deployment, it still fails. This is a perfect example of the **Principle of Least Privilege**. We granted **`list`** and **`get`**, but not **`create`**. When troubleshooting RBAC, always check that the specific **verb** and **resource** in your Role match what the app is actually trying to do.

---

Finally, let’s talk about **Scope**. A **RoleBinding** is namespaced. If **`dev-user`** has permissions in the **`rbac-lab`** namespace, they are still completely **Forbidden** from listing pods in **`default`**. 

This is where the distinction between **Roles** and **ClusterRoles** is critical. If you need a user to have access across the **entire cluster** (all namespaces), you must use a **ClusterRoleBinding**. If you only need them to have access to specific namespaces, you need a separate **RoleBinding** in each one.

---

**Cleanup**

**Delete** **`rbac-lab`**.

---

**Closing**

**Forbidden** → **`auth can-i`**, **`describe rolebinding`**, **`describe clusterrolebinding`**. **Least privilege** — **grant** only what **users** and **service accounts** **need**.

Thanks for watching.
