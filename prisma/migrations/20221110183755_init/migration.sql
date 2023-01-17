-- CreateTable
CREATE TABLE "CatalogGuy" (
    "id" SERIAL NOT NULL,
    "Name" TEXT NOT NULL,
    "ID_DC" TEXT NOT NULL,
    "user_role" TEXT[],

    CONSTRAINT "CatalogGuy_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "test" (
    "id" SERIAL NOT NULL,
    "Name" TEXT NOT NULL,
    "ID_DC" TEXT NOT NULL,
    "user_role" TEXT[],
    "tg_channel" TEXT,
    "skill_level" TEXT[],

    CONSTRAINT "test_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "test_Name_key" ON "test"("Name");
